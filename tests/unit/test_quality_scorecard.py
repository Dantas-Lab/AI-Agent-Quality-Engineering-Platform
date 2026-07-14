import pytest

from quality.scorecards.calculator import calculate_quality_score


@pytest.mark.unit
def test_calculate_quality_score() -> None:
    metrics = {
        "correctness": 1.0,
        "faithfulness": 0.8,
        "relevance": 0.9,
        "completeness": 0.7,
        "safety": 1.0,
        "source_attribution": 1.0,
        "latency": 0.8,
    }

    score = calculate_quality_score(metrics)

    assert score == 0.89
