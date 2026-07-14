import json
from pathlib import Path

import pytest

from quality.analyzers.conversation_analyzer import ConversationAnalysis
from quality.analyzers.scorecard_reporter import (
    build_quality_report,
    save_quality_report,
)


@pytest.mark.unit
def test_build_and_save_quality_report(
    tmp_path: Path,
) -> None:
    analysis = ConversationAnalysis(
        total_cases=5,
        passed_cases=4,
        failed_cases=1,
        pass_rate=0.8,
        average_score=0.9,
    )

    failures = {
        "missing_information": 1,
    }

    report = build_quality_report(
        analysis,
        failures,
    )

    output_path = tmp_path / "quality-report.json"

    save_quality_report(
        report,
        output_path,
    )

    saved_report = json.loads(output_path.read_text(encoding="utf-8"))

    assert saved_report["summary"]["total_cases"] == 5
    assert saved_report["summary"]["pass_rate"] == 0.8
    assert saved_report["failure_distribution"] == failures
