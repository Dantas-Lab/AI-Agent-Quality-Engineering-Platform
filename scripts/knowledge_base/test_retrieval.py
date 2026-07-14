from app.rag.retriever import Retriever
from app.rag.vector_store import VectorStore


def test_retrieval() -> None:
    vector_store = VectorStore()
    retriever = Retriever(vector_store)

    results = retriever.retrieve(
        "Quais documentos preciso para atualizar meu cadastro?"
    )

    for result in results:
        print(f"Source: {result.source}")
        print(f"Distance: {result.distance}")
        print("---")


if __name__ == "__main__":
    test_retrieval()
