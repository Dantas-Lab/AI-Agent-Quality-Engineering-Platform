from dataclasses import dataclass

from quality.release_gate.criteria import RELEASE_CRITERIA


@dataclass
class ReleaseEvaluation:
    approved: bool
    failed_criteria: list[str]


def evaluate_release(
    overall_score: float,
    hallucination_rate: float,
    critical_failures: int,
    regression_pass_rate: float,
    safety_score: float,
) -> ReleaseEvaluation:
    failed_criteria = []

    if overall_score < RELEASE_CRITERIA["minimum_overall_score"]:
        failed_criteria.append("minimum_overall_score")

    if hallucination_rate > RELEASE_CRITERIA["maximum_hallucination_rate"]:
        failed_criteria.append("maximum_hallucination_rate")

    if critical_failures > RELEASE_CRITERIA["maximum_critical_failures"]:
        failed_criteria.append("maximum_critical_failures")

    if regression_pass_rate < RELEASE_CRITERIA["minimum_regression_pass_rate"]:
        failed_criteria.append("minimum_regression_pass_rate")

    if safety_score < RELEASE_CRITERIA["minimum_safety_score"]:
        failed_criteria.append("minimum_safety_score")

    return ReleaseEvaluation(
        approved=not failed_criteria,
        failed_criteria=failed_criteria,
    )
