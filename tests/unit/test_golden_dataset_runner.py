from pathlib import Path

import pytest

from quality.evaluators.golden_dataset_runner import (
    GoldenDatasetRunner,
)


@pytest.mark.unit
def test_golden_dataset_case_passes() -> None:
    runner = GoldenDatasetRunner(Path("datasets/golden/golden_dataset.json"))

    case = runner.load_dataset()[0]

    result = runner.evaluate_case(
        case=case,
        answer=(
            "Documento oficial de identificação, CPF "
            "e comprovante de residência são necessários."
        ),
        retrieved_sources=["cadastro.md"],
    )

    assert result.passed is True
