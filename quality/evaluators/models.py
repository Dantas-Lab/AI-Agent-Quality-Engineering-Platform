from dataclasses import dataclass, field


@dataclass
class MetricResult:
    name: str
    score: float
    passed: bool
    reason: str


@dataclass
class EvaluationResult:
    case_id: str
    passed: bool
    metrics: list[MetricResult] = field(default_factory=list)
