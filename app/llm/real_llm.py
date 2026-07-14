import os
from typing import cast

from openai import OpenAI


class RealLLM:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
        )

        return cast(str, response.output_text)
