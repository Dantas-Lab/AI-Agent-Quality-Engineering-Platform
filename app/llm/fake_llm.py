class FakeLLM:
    def generate(self, prompt: str) -> str:
        return f"Fake LLM response for: {prompt}"

    def generate_response(self, message: str) -> str:
        return self.generate(message)
