import pytest

from app.llm.fake_llm import FakeLLM


@pytest.mark.unit
@pytest.mark.parametrize(
    ("prompt", "expected_response"),
    [
        ("Hello", "Fake LLM response for: Hello"),
        (
            "How can I update my registration?",
            "Fake LLM response for: How can I update my registration?",
        ),
        ("", "Fake LLM response for: "),
    ],
)
def test_fake_llm_parametrized(
    fake_llm: FakeLLM,
    prompt: str,
    expected_response: str,
) -> None:
    response = fake_llm.generate_response(prompt)

    assert response == expected_response
