from typing import Any, cast

import chromadb
from chromadb.api.models.Collection import Collection


class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db") -> None:
        self.client = chromadb.PersistentClient(path=persist_directory)

        self.collection: Collection = self.client.get_or_create_collection(
            name="citizen_services",
        )

    def add_documents(self, documents: list[dict[str, str]]) -> None:
        self.collection.upsert(
            ids=[document["id"] for document in documents],
            documents=[document["content"] for document in documents],
            metadatas=[{"source": document["source"]} for document in documents],
        )

    def query(
        self,
        query_text: str,
        n_results: int = 3,
    ) -> dict[str, Any]:
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
        )

        return cast(dict[str, Any], results)
