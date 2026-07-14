import os
from typing import cast

from openai import OpenAI


class RealLLM:
    def __init__(self) -> None:
        api_key = os.getenv("LLM_API_KEY")

        if not api_key:
            raise ValueError("LLM_API_KEY is not configured.")

        self.client = OpenAI(api_key=api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )

        return cast(str, response.output_text)
