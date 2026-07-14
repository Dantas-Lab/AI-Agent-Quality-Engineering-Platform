import pytest

from quality.evaluators.retrieval import (
    evaluate_expected_sources,
    evaluate_retrieval_hit,
)


@pytest.mark.unit
def test_expected_sources_pass() -> None:
    result = evaluate_expected_sources(
        retrieved_sources=["cadastro.md", "prazos.md"],
        expected_sources=["cadastro.md"],
    )

    assert result.passed is True
    assert result.score == 1.0


@pytest.mark.unit
def test_retrieval_hit_pass() -> None:
    result = evaluate_retrieval_hit(
        retrieved_sources=["cadastro.md"],
        expected_sources=["cadastro.md"],
    )

    assert result.passed is True
