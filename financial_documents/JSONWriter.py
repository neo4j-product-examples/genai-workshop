import json
import logging
from typing import Optional
from neo4j_graphrag.experimental.components.kg_writer import (
    KGWriter,
    KGWriterModel,
)
from pydantic import validate_call
from neo4j_graphrag.experimental.components.types import (
    LexicalGraphConfig,
    Neo4jGraph,
)
logger = logging.getLogger(__name__)

class JSONWriter(KGWriter):
    """Writes a knowledge graph to a JSON file."""

    def __init__(
        self,
        output_path: str,
        clean_file: bool = True,
    ):
        self.output_path = output_path
        self.clean_file = clean_file

    @validate_call
    async def run(
        self,
        graph: Neo4jGraph,
        lexical_graph_config: LexicalGraphConfig = LexicalGraphConfig(),
    ) -> KGWriterModel:
        """Serializes a knowledge graph to a JSON file."""
        try:
            data = {
                "nodes": [node.model_dump() for node in graph.nodes],
                "relationships": [rel.model_dump() for rel in graph.relationships],
            }

            if self.clean_file:
                # Overwrite the file if clean_file is True
                mode = "w"
            else:
                # Append to the file (not typical for JSON, but shown for completeness)
                mode = "a"

            with open(self.output_path, mode, encoding="utf-8") as f:
                json.dump(data, f, indent=2)

            return KGWriterModel(
                status="SUCCESS",
                metadata={
                    "node_count": len(graph.nodes),
                    "relationship_count": len(graph.relationships),
                    "output_path": self.output_path,
                },
            )
        except Exception as e:
            logger.exception(e)
            return KGWriterModel(status="FAILURE", metadata={"error": str(e)})