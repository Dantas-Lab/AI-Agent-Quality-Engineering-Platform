import pytest

from quality.release_gate.evaluator import evaluate_release


@pytest.mark.unit
def test_release_is_approved_when_all_criteria_pass() -> None:
    result = evaluate_release(
        overall_score=0.90,
        hallucination_rate=0.01,
        critical_failures=0,
        regression_pass_rate=0.98,
        safety_score=1.00,
    )

    assert result.approved is True
    assert result.failed_criteria == []


@pytest.mark.unit
def test_release_is_rejected_when_criteria_fail() -> None:
    result = evaluate_release(
        overall_score=0.80,
        hallucination_rate=0.05,
        critical_failures=1,
        regression_pass_rate=0.90,
        safety_score=0.95,
    )

    assert result.approved is False
    assert "minimum_overall_score" in result.failed_criteria
    assert "maximum_hallucination_rate" in result.failed_criteria
    assert "maximum_critical_failures" in result.failed_criteria
    assert "minimum_regression_pass_rate" in result.failed_criteria
    assert "minimum_safety_score" in result.failed_criteria
