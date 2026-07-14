from app.llm.base import LLMProvider
from app.rag.prompt_builder import PromptBuilder
from app.rag.retriever import RetrievedDocument, Retriever


class RAGPipeline:
    def __init__(
        self,
        retriever: Retriever,
        prompt_builder: PromptBuilder,
        llm: LLMProvider,
    ) -> None:
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def run(self, question: str) -> tuple[str, list[RetrievedDocument]]:
        documents = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question=question,
            documents=documents,
        )

        answer = self.llm.generate_response(prompt)

        return answer, documents
