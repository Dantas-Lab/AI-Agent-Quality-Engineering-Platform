from dataclasses import dataclass

from quality.evaluators.models import EvaluationResult


@dataclass
class ConversationAnalysis:
    total_cases: int
    passed_cases: int
    failed_cases: int
    pass_rate: float
    average_score: float


def analyze_evaluation_results(
    results: list[EvaluationResult],
) -> ConversationAnalysis:
    total_cases = len(results)

    if total_cases == 0:
        return ConversationAnalysis(
            total_cases=0,
            passed_cases=0,
            failed_cases=0,
            pass_rate=0.0,
            average_score=0.0,
        )

    passed_cases = sum(result.passed for result in results)
    failed_cases = total_cases - passed_cases

    metric_scores = [metric.score for result in results for metric in result.metrics]

    average_score = sum(metric_scores) / len(metric_scores) if metric_scores else 0.0

    return ConversationAnalysis(
        total_cases=total_cases,
        passed_cases=passed_cases,
        failed_cases=failed_cases,
        pass_rate=round(passed_cases / total_cases, 4),
        average_score=round(average_score, 4),
    )
