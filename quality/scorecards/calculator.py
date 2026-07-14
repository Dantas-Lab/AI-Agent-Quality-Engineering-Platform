from quality.scorecards.weights import QUALITY_WEIGHTS


def calculate_quality_score(metrics: dict[str, float]) -> float:
    weighted_score = sum(
        metrics[metric] * weight for metric, weight in QUALITY_WEIGHTS.items()
    )

    return round(weighted_score, 4)
