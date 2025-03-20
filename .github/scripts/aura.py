import argparse
import os
import json
import time
import logging

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


class AuraAPI:
    def __init__(self, url, tenant_id, token=None, **kwargs):
        self.url = url
        self.token = token
        self.tenant_id = tenant_id
        self.config = kwargs

    def status(self, instance_id):
        headers = {"Content-Type": "application/json", "Authorization": self.token}
        _url = os.path.join(self.url, instance_id)
        response = requests.get(_url, headers=headers)
        res = json.loads(response.content)
        if not res.get('data'):
            logger.info("Unable to retrieve instance Status : {}".format(instance_id))
            return 'Unknown'
        status = res.get('data').get('status')
        return status

    def create(self, params):
        headers = {"Content-Type": "application/json", "Authorization": self.token}
        params.update({
            'tenant_id': self.tenant_id
        })
        response = requests.post(self.url, headers=headers, json=params)
        res = json.loads(response.content)
        instance_details = res.get('data', {})
        errors = res.get('errors', {})
        if not instance_details:
            logger.info("Instance creation not successful: {}".format(errors))
        return instance_details

    def delete(self, instance_id):
        _url = os.path.join(self.url, instance_id)
        headers = {"Content-Type": "application/json", "Authorization": self.token}
        response = requests.delete(_url, headers=headers)
        res = json.loads(response.content)
        instance_details = res.get('data', {})
        errors = res.get('errors', {})
        if not instance_details:
            logger.info("Instance not found or unable to delete: {}".format(errors))
            return dict()
        return instance_details

    def generate_token(self, url, client_id, client_secret):
        body = {
            "grant_type": "client_credentials"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, auth=(client_id, client_secret), headers=headers, data=body)
        data = json.loads(response.content)
        token = data['access_token']
        return token

    def generate_token_if_expired(self):
        auth_config = self.config['auth']
        auth_url = auth_config.get('endpoint')
        client_id = auth_config.get('client_id')
        client_secret = auth_config.get('client_secret')
        if time.time() - auth_config.get('token_ttl') >= 3599:
            self.token = self.generate_token(auth_url, client_id, client_secret)
            self.config['auth']['access_token'] = self.token
            self.config['auth']['token_ttl'] = time.time()
            logger.info("Token Generation Successful: {}".format(time.ctime()))
            return True
        logger.info("Token is Valid")
        return False

    def wait_for_status(self, instance_id, status=None, time_out=300):
        start = time.time()
        current_status = self.status(instance_id)
        while current_status != status and time.time() - start <= time_out:
            time.sleep(5)
            current_status = self.status(instance_id)
            logger.info("Waiting: {} {}".format(instance_id, current_status))
        return current_status


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('task', type=str, help='setup task', choices=['configure', 'delete'])
    parser.add_argument('--tenant-id', type=str, help="Aura Tenant ID")
    parser.add_argument('--client-id', type=str, help="Aura API Client ID")
    parser.add_argument('--client-secret', type=str, help="Aura API Client Secret")
    parser.add_argument('--region', type=str, help="Aura Region")
    parser.add_argument('--cloud-provider', type=str, help="Aura Cloud Provider")
    parser.add_argument('--instance-id', type=str, help="Aura Instance Id")

    return parser.parse_args()


def configure_instance(api, region, cloud_provider):
    logger.info("Creating Aura instance")
    data = api.create(params={
        "name": "gh-action-genai-workshop",
        "version": "5",
        "region": region,
        "memory": "8GB",
        "type": "enterprise-ds",
        "cloud_provider": cloud_provider,
    })
    instance_details = {k: v for k, v in data.items() if
                        k in ['id', 'connection_url', 'name', 'username', 'password']}
    logger.info(f"Waiting for Aura instance {instance_details['id']} to come online")
    api.wait_for_status(instance_details['id'], status="running", time_out=300)

    print(f"""
AURA_INSTANCEID={instance_details['id']}
NEO4J_URI={instance_details['connection_url']}
NEO4J_USERNAME={instance_details['username']}
NEO4J_PASSWORD={instance_details['password']}
AURA_DS=true
""")


def delete_instance(api, instance_id):
    logger.info(f"Deleting Aura instance {instance_id}")
    api.delete(instance_id)


if __name__ == '__main__':
    args = cli()

    config = {
        "auth": {
            "endpoint": "https://api.neo4j.io/oauth/token",
            "client_id": args.client_id,
            "client_secret": args.client_secret,
            "token_ttl": 0.0
        }
    }
    api = AuraAPI("https://api.neo4j.io/v1/instances", args.tenant_id, **config)
    _ = api.generate_token_if_expired()

    task = args.task
    if task == 'configure':
        configure_instance(api, args.region, args.cloud_provider)

    if task == 'delete':
        delete_instance(api, args.instance_id)
