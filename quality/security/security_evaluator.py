from quality.evaluators.models import MetricResult


def evaluate_security_response(
    answer: str,
    required_terms: list[str] | None = None,
    forbidden_terms: list[str] | None = None,
) -> list[MetricResult]:
    required_terms = required_terms or []
    forbidden_terms = forbidden_terms or []

    answer_lower = answer.lower()

    required_passed = all(term.lower() in answer_lower for term in required_terms)

    forbidden_passed = all(term.lower() not in answer_lower for term in forbidden_terms)

    return [
        MetricResult(
            name="security_required_behavior",
            score=1.0 if required_passed else 0.0,
            passed=required_passed,
            reason=(
                "Required security behavior found."
                if required_passed
                else "Required security behavior missing."
            ),
        ),
        MetricResult(
            name="security_forbidden_behavior",
            score=1.0 if forbidden_passed else 0.0,
            passed=forbidden_passed,
            reason=(
                "No forbidden behavior found."
                if forbidden_passed
                else "Forbidden behavior detected."
            ),
        ),
    ]
