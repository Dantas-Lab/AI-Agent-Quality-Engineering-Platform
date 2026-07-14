from quality.evaluators.models import EvaluationResult

METRIC_FAILURE_MAPPING = {
    "required_terms": "missing_information",
    "forbidden_terms": "hallucination",
    "empty_response": "missing_information",
    "expected_sources": "incorrect_source_attribution",
    "retrieval_hit": "incorrect_retrieval",
}


def classify_failures(
    results: list[EvaluationResult],
) -> dict[str, int]:
    failures: dict[str, int] = {}

    for result in results:
        for metric in result.metrics:
            if metric.passed:
                continue

            failure_category = METRIC_FAILURE_MAPPING.get(
                metric.name,
                "unclassified_failure",
            )

            failures[failure_category] = failures.get(failure_category, 0) + 1

    return failures
