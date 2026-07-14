import os

from app.llm.fake_llm import FakeLLM
from app.llm.real_llm import RealLLM


def create_llm() -> FakeLLM | RealLLM:
    provider = os.getenv("LLM_PROVIDER", "fake").lower()

    if provider == "real":
        return RealLLM()

    return FakeLLM()
