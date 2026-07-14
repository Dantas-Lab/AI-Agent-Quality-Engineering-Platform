import pytest

from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import RetrievedDocument


@pytest.mark.unit
def test_prompt_builder_includes_question_and_context() -> None:
    builder = PromptBuilder()

    documents = [
        RetrievedDocument(
            content="The registration update requires an ID document.",
            source="cadastro.md",
            distance=0.1,
        )
    ]

    prompt = builder.build(
        question="Which documents are required?",
        documents=documents,
    )

    assert "Which documents are required?" in prompt
    assert "cadastro.md" in prompt
    assert "The registration update requires an ID document." in prompt
