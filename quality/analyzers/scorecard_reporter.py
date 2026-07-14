import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from quality.analyzers.conversation_analyzer import (
    ConversationAnalysis,
)


def build_quality_report(
    analysis: ConversationAnalysis,
    failures: dict[str, int],
) -> dict[str, Any]:
    return {
        "summary": asdict(analysis),
        "failure_distribution": failures,
    }


def save_quality_report(
    report: dict[str, Any],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as report_file:
        json.dump(
            report,
            report_file,
            indent=2,
        )
