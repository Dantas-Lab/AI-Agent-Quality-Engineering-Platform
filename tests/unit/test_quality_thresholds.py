import pytest

from quality.scorecards.validator import validate_metrics


@pytest.mark.unit
def test_validate_metrics_against_thresholds() -> None:
    metrics = {
        "overall_score": 0.88,
        "correctness": 0.90,
        "faithfulness": 0.82,
        "safety": 1.00,
    }

    result = validate_metrics(metrics)

    assert result["overall_score"] is True
    assert result["correctness"] is True
    assert result["faithfulness"] is False
    assert result["safety"] is True
