from quality.evaluators.models import MetricResult


def evaluate_expected_sources(
    retrieved_sources: list[str],
    expected_sources: list[str],
) -> MetricResult:
    if not expected_sources:
        passed = not retrieved_sources

        return MetricResult(
            name="expected_sources",
            score=1.0 if passed else 0.0,
            passed=passed,
            reason=(
                "No sources expected or retrieved."
                if passed
                else f"Unexpected sources retrieved: {retrieved_sources}"
            ),
        )

    matched_sources = [
        source for source in expected_sources if source in retrieved_sources
    ]

    score = len(matched_sources) / len(expected_sources)
    passed = score == 1.0

    missing_sources = [
        source for source in expected_sources if source not in retrieved_sources
    ]

    return MetricResult(
        name="expected_sources",
        score=score,
        passed=passed,
        reason=(
            "All expected sources retrieved."
            if passed
            else f"Missing sources: {missing_sources}"
        ),
    )


def evaluate_retrieval_hit(
    retrieved_sources: list[str],
    expected_sources: list[str],
) -> MetricResult:
    hit = any(source in retrieved_sources for source in expected_sources)

    return MetricResult(
        name="retrieval_hit",
        score=1.0 if hit else 0.0,
        passed=hit,
        reason=("Expected source found." if hit else "No expected source found."),
    )
