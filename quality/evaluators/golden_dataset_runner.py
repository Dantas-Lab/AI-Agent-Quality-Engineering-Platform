import json
from pathlib import Path
from typing import Any

from quality.evaluators.deterministic import (
    evaluate_empty_response,
    evaluate_forbidden_terms,
    evaluate_required_terms,
)
from quality.evaluators.models import EvaluationResult
from quality.evaluators.retrieval import evaluate_expected_sources


class GoldenDatasetRunner:
    def __init__(self, dataset_path: Path) -> None:
        self.dataset_path = dataset_path

    def load_dataset(self) -> list[dict[str, Any]]:
        with self.dataset_path.open(encoding="utf-8") as dataset_file:
            data: list[dict[str, Any]] = json.load(dataset_file)

        return data

    def evaluate_case(
        self,
        case: dict[str, Any],
        answer: str,
        retrieved_sources: list[str],
    ) -> EvaluationResult:
        metrics = [
            evaluate_empty_response(answer),
            evaluate_required_terms(
                answer,
                case["must_include"],
            ),
            evaluate_forbidden_terms(
                answer,
                case["must_not_include"],
            ),
            evaluate_expected_sources(
                retrieved_sources,
                case["expected_sources"],
            ),
        ]

        return EvaluationResult(
            case_id=case["id"],
            passed=all(metric.passed for metric in metrics),
            metrics=metrics,
        )
