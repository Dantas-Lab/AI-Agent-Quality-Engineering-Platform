import pytest

from quality.analyzers.conversation_analyzer import (
    analyze_evaluation_results,
)
from quality.evaluators.models import EvaluationResult, MetricResult


@pytest.mark.unit
def test_analyze_evaluation_results() -> None:
    results = [
        EvaluationResult(
            case_id="GD-001",
            passed=True,
            metrics=[
                MetricResult(
                    name="required_terms",
                    score=1.0,
                    passed=True,
                    reason="Passed",
                )
            ],
        ),
        EvaluationResult(
            case_id="GD-002",
            passed=False,
            metrics=[
                MetricResult(
                    name="required_terms",
                    score=0.0,
                    passed=False,
                    reason="Failed",
                )
            ],
        ),
    ]

    analysis = analyze_evaluation_results(results)

    assert analysis.total_cases == 2
    assert analysis.passed_cases == 1
    assert analysis.failed_cases == 1
    assert analysis.pass_rate == 0.5
    assert analysis.average_score == 0.5
