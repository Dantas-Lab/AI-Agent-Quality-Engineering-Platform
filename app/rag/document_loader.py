from pathlib import Path


class DocumentLoader:
    def __init__(self, documents_path: Path) -> None:
        self.documents_path = documents_path

    def load_documents(self) -> list[dict[str, str]]:
        documents = []

        for file_path in self.documents_path.glob("*.md"):
            documents.append(
                {
                    "id": file_path.stem,
                    "content": file_path.read_text(encoding="utf-8"),
                    "source": file_path.name,
                }
            )

        return documents
