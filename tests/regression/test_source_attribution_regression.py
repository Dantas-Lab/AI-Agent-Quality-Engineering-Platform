import pytest

from app.rag.retriever import Retriever
from app.rag.vector_store import VectorStore


@pytest.mark.regression
@pytest.mark.rag
def test_retrieved_documents_have_source_attribution() -> None:
    vector_store = VectorStore()
    retriever = Retriever(vector_store)

    documents = retriever.retrieve("Como solicitar a segunda via de um documento?")

    assert documents

    for document in documents:
        assert document.source
        assert document.source.strip()
