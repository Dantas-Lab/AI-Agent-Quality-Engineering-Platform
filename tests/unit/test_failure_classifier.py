import pytest

from quality.analyzers.failure_classifier import classify_failures
from quality.evaluators.models import EvaluationResult, MetricResult


@pytest.mark.unit
def test_classify_failures() -> None:
    results = [
        EvaluationResult(
            case_id="GD-001",
            passed=False,
            metrics=[
                MetricResult(
                    name="required_terms",
                    score=0.0,
                    passed=False,
                    reason="Missing terms",
                ),
                MetricResult(
                    name="expected_sources",
                    score=0.0,
                    passed=False,
                    reason="Missing source",
                ),
            ],
        )
    ]

    failures = classify_failures(results)

    assert failures["missing_information"] == 1
    assert failures["incorrect_source_attribution"] == 1
