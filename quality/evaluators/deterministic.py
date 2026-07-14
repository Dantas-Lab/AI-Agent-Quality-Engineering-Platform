from quality.evaluators.models import MetricResult


def evaluate_required_terms(
    answer: str,
    required_terms: list[str],
) -> MetricResult:
    answer_lower = answer.lower()

    missing_terms = [
        term for term in required_terms if term.lower() not in answer_lower
    ]

    passed = not missing_terms

    return MetricResult(
        name="required_terms",
        score=1.0 if passed else 0.0,
        passed=passed,
        reason=(
            "All required terms found." if passed else f"Missing terms: {missing_terms}"
        ),
    )


def evaluate_forbidden_terms(
    answer: str,
    forbidden_terms: list[str],
) -> MetricResult:
    answer_lower = answer.lower()

    found_terms = [term for term in forbidden_terms if term.lower() in answer_lower]

    passed = not found_terms

    return MetricResult(
        name="forbidden_terms",
        score=1.0 if passed else 0.0,
        passed=passed,
        reason=(
            "No forbidden terms found."
            if passed
            else f"Forbidden terms found: {found_terms}"
        ),
    )


def evaluate_empty_response(answer: str) -> MetricResult:
    passed = bool(answer.strip())

    return MetricResult(
        name="empty_response",
        score=1.0 if passed else 0.0,
        passed=passed,
        reason=("Response is not empty." if passed else "Response is empty."),
    )
