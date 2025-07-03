# PDF Loader Script for Neo4j GraphRAG
# This script focuses solely on loading PDF files into Neo4j

from neo4j import GraphDatabase
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.generation.prompts import ERExtractionTemplate
from dotenv import load_dotenv
import os
import time
import asyncio
import glob
import csv

# --- Neo4j Connection ---
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Using OpenAI cloud backend")
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# --- Load Approved Company Names ---
approved_companies = set()
with open('data/Company_Filings.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row.get('name')
        if name:
            approved_companies.add(name.strip().upper())

# --- Initialize LLM and Embeddings ---
# Never hardcode API keys, always use environment variables
llm = OpenAILLM(
    model_name="gpt-3.5-turbo",
    api_key=OPENAI_API_KEY
)
dimensions = 1536
embedder = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

# --- Custom ERExtractionTemplate for KG Builder ---
joined_names = '\n'.join(f"- {name}" for name in approved_companies)
company_instruction = (
    "Extract only information about the following companies. "
    "If a company is mentioned but is not in this list, ignore it. "
    "When extracting, the company name must match exactly as shown below. "
    "Do not generate or include any company not on this list or an alternate name for any company on this list. "
    "ONLY USE THE COMPANY NAME EXACTLY AS SHOWN IN THE LIST. "
    "If the text refers to 'the Company', 'the Registrant', or uses a pronoun or generic phrase instead of a company name, you MUST look up and use the exact company name from the allowed list based on context (such as the file being processed). "
    "UNDER NO CIRCUMSTANCES should you output 'the Company', 'the Registrant', or any generic phrase as a company name. Only use the exact allowed company name.\n\n"
    f"Allowed Companies (match exactly):\n{joined_names}\n\n"
    "\nIMPORTANT: When returning the 'properties' field for any entity or relationship, always use a JSON object (e.g., {{}}), even if there are no properties. Never use an empty array ([]). If there are no properties, return 'properties': {{}}.\n"
)
custom_template = company_instruction + ERExtractionTemplate.DEFAULT_TEMPLATE
prompt_template = ERExtractionTemplate(template=custom_template)

# --- Define Node Labels and Relationship Types ---
entities = [
    {"label": "Executive", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "Product", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "FinancialMetric", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "RiskFactor", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "StockType", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "Transaction", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "TimePeriod", "properties": [{"name": "name", "type": "STRING"}]},
    {"label": "Company", "properties": [{"name": "name", "type": "STRING"}]}
]
relations = [
    {"label": "HAS_METRIC", "source": "Company", "target": "FinancialMetric"},
    {"label": "FACES_RISK", "source": "Company", "target": "RiskFactor"},
    {"label": "ISSUED_STOCK", "source": "Company", "target": "StockType"},
    {"label": "MENTIONS", "source": "Company", "target": "Product"}  # Adjust as needed
]

# --- Initialize and Run the Pipeline ---
print("Entities being passed to pipeline:", entities)
print("Type of entities:", type(entities))

try:
    pipeline = SimpleKGPipeline(
        driver=driver,
        llm=llm,
        embedder=embedder,
        entities=entities,
        relations=relations,
        prompt_template=prompt_template,
        enforce_schema="STRICT"  # Use "STRICT" for schema enforcement mode
    )
except Exception as e:
    print("Pipeline initialization failed:", e)
    raise

# --- Async Pipeline Run Example ---
async def run_pipeline_on_file(file_path, pipeline):
    await pipeline.run_async(file_path=file_path)

# Run the pipeline on all files in data/form10k-sample before retrieval
form10k_dir = "data/form10k-sample"
pdf_files = glob.glob(form10k_dir + "/*.pdf")

print(f"\nFound {len(pdf_files)} PDF files to process")
for pdf_file in pdf_files:
    try:
        print(f"\nProcessing file: {pdf_file}")
        asyncio.run(run_pipeline_on_file(pdf_file, pipeline))
        print(f"Successfully processed: {pdf_file}")
        time.sleep(21)  # Add a delay between requests to avoid hitting OpenAI's RPM limit
    except Exception as e:
        print(f"Error processing {pdf_file}: {str(e)}")
        print("Continuing with next file...")
        continue

print("\nPDF loading complete!")



with driver.session() as session:
    try:
        create_index_query = """
        CREATE VECTOR INDEX riskfactor_vector_index
        FOR (r:RiskFactor)
        ON (r.embedding)
        OPTIONS {
        indexConfig: {
            `vector.dimensions`: 1536,
            `vector.similarity_function`: 'cosine'
        }
        }
        """
        session.run(create_index_query)
        print("Successfully created vector index 'chunkEmbeddings'")
    except Exception as e:
        print("Vector index already created:", e)
    driver.close()

    ## -- Now head to http://console.neo4j.io and upload the structured data from the data folder
    ## -- Use the neo4j_importer_model.json as the model