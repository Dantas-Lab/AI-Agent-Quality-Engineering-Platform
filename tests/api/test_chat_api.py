import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
def test_chat_endpoint_returns_successful_response(
    api_client: TestClient,
) -> None:
    payload = {
        "message": "How can I update my registration?",
        "session_id": "api-test-session",
    }

    response = api_client.post("/chat", json=payload)

    response_data = response.json()

    assert response.status_code == 200
    assert "answer" in response_data
    assert "sources" in response_data
    assert response_data["session_id"] == "api-test-session"


@pytest.mark.api
@pytest.mark.parametrize(
    "payload",
    [
        {"session_id": "missing-message"},
        {"message": "Hello"},
        {"message": "", "session_id": "empty-message"},
        {"message": 123, "session_id": "invalid-message-type"},
    ],
)
def test_chat_endpoint_rejects_invalid_payloads(
    api_client: TestClient,
    payload: dict[str, object],
) -> None:
    response = api_client.post("/chat", json=payload)

    assert response.status_code == 422
