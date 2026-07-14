import pytest

from app.rag.retriever import Retriever
from app.rag.vector_store import VectorStore


@pytest.mark.regression
@pytest.mark.rag
def test_registration_question_retrieves_expected_document() -> None:
    vector_store = VectorStore()
    retriever = Retriever(vector_store)

    documents = retriever.retrieve(
        "Quais documentos preciso para atualizar meu cadastro?"
    )

    sources = [document.source for document in documents]

    assert "cadastro.md" in sources
