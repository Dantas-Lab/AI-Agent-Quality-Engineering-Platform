from quality.thresholds import QUALITY_THRESHOLDS


def validate_metrics(metrics: dict[str, float]) -> dict[str, bool]:
    return {
        metric: metrics[metric] >= threshold
        for metric, threshold in QUALITY_THRESHOLDS.items()
        if metric in metrics
    }
