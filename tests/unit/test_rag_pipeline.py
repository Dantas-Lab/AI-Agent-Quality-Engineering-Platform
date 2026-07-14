from unittest.mock import Mock

import pytest

from app.rag.pipeline import RAGPipeline
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import RetrievedDocument


@pytest.mark.unit
def test_rag_pipeline_uses_retriever_and_llm() -> None:
    retrieved_documents = [
        RetrievedDocument(
            content="Registration requires an ID document.",
            source="cadastro.md",
            distance=0.1,
        )
    ]

    retriever = Mock()
    retriever.retrieve.return_value = retrieved_documents

    llm = Mock()
    llm.generate_response.return_value = "Generated answer"

    pipeline = RAGPipeline(
        retriever=retriever,
        prompt_builder=PromptBuilder(),
        llm=llm,
    )

    answer, documents = pipeline.run("Which documents are required?")

    assert answer == "Generated answer"
    assert documents == retrieved_documents

    retriever.retrieve.assert_called_once_with("Which documents are required?")

    llm.generate_response.assert_called_once()
