import pytest

from app.llm.fake_llm import FakeLLM


@pytest.mark.unit
def test_fake_llm_returns_deterministic_response(fake_llm: FakeLLM) -> None:
    prompt = "Hello"

    response = fake_llm.generate_response(prompt)

    assert response == "Fake LLM response for: Hello"
