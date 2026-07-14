import pytest

from quality.evaluators.deterministic import (
    evaluate_empty_response,
    evaluate_forbidden_terms,
    evaluate_required_terms,
)


@pytest.mark.unit
def test_required_terms_pass() -> None:
    result = evaluate_required_terms(
        "CPF and ID document are required.",
        ["CPF", "ID document"],
    )

    assert result.passed is True
    assert result.score == 1.0


@pytest.mark.unit
def test_forbidden_terms_fail() -> None:
    result = evaluate_forbidden_terms(
        "There is a mandatory fee.",
        ["mandatory fee"],
    )

    assert result.passed is False
    assert result.score == 0.0


@pytest.mark.unit
def test_empty_response_fail() -> None:
    result = evaluate_empty_response("")

    assert result.passed is False
