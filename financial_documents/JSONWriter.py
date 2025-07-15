import json
from pydantic import validate_call
from neo4j_graphrag.experimental.components.kg_writer import (
    KGWriter,
    KGWriterModel,
)
from neo4j_graphrag.experimental.components.types import Neo4jGraph

class JsonWriter(KGWriter):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @validate_call
    async def run(self, graph: Neo4jGraph) -> KGWriterModel:
        try:
            with open(self.file_name, "w") as f:
                json.dump(graph.model_dump(), f, indent=2)
            return KGWriterModel(status="SUCCESS")
        except Exception:
            return KGWriterModel(status="FAILURE")