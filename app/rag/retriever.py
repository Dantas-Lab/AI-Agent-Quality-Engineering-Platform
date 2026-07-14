from dataclasses import dataclass

from app.rag.vector_store import VectorStore


@dataclass
class RetrievedDocument:
    content: str
    source: str
    distance: float


class Retriever:
    def __init__(self, vector_store: VectorStore) -> None:
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        n_results: int = 3,
    ) -> list[RetrievedDocument]:
        results = self.vector_store.query(
            query_text=query,
            n_results=n_results,
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        return [
            RetrievedDocument(
                content=document,
                source=metadata["source"],
                distance=distance,
            )
            for document, metadata, distance in zip(
                documents,
                metadatas,
                distances,
                strict=True,
            )
        ]
