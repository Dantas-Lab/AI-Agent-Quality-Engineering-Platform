from pathlib import Path

from app.rag.document_loader import DocumentLoader
from app.rag.vector_store import VectorStore


def ingest_documents() -> None:
    documents_path = Path("knowledge_base/documents")

    loader = DocumentLoader(documents_path)
    documents = loader.load_documents()

    vector_store = VectorStore()
    vector_store.add_documents(documents)

    print(f"Successfully ingested {len(documents)} documents.")


if __name__ == "__main__":
    ingest_documents()
