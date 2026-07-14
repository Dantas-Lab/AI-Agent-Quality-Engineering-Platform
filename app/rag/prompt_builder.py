from app.rag.retriever import RetrievedDocument


class PromptBuilder:
    def build(
        self,
        question: str,
        documents: list[RetrievedDocument],
    ) -> str:
        context = "\n\n".join(
            f"Source: {document.source}\n{document.content}" for document in documents
        )

        return (
            "Answer the user's question using only the provided context.\n"
            "If the context is insufficient, say that you do not have "
            "enough information.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}"
        )
