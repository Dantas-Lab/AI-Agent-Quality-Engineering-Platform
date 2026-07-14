class FakeLLM:
    def generate_response(self, message: str) -> str:
        return f"Fake LLM response for: {message}"
