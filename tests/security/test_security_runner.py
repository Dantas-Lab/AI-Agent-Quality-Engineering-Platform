from pathlib import Path

import pytest

from quality.security.security_runner import SecurityTestRunner


@pytest.mark.security
def test_security_runner_evaluates_case() -> None:
    runner = SecurityTestRunner(Path("datasets/security/adversarial_dataset.json"))

    case = runner.load_dataset()[2]

    result = runner.evaluate_case(
        case=case,
        answer=("Não posso fornecer dados pessoais de outros clientes."),
    )

    assert result.case_id == "SEC-003"
    assert result.passed is True
