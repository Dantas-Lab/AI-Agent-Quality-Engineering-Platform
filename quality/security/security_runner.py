import json
from pathlib import Path
from typing import Any

from quality.evaluators.models import EvaluationResult
from quality.security.security_evaluator import (
    evaluate_security_response,
)


class SecurityTestRunner:
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
    ) -> EvaluationResult:
        metrics = evaluate_security_response(
            answer=answer,
            required_terms=case.get("required_terms"),
            forbidden_terms=case.get("forbidden_terms"),
        )

        return EvaluationResult(
            case_id=case["id"],
            passed=all(metric.passed for metric in metrics),
            metrics=metrics,
        )
