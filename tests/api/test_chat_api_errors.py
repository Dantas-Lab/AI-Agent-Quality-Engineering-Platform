from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
def test_chat_endpoint_returns_server_error_when_llm_fails(
    api_client: TestClient,
) -> None:
    payload = {
        "message": "Hello",
        "session_id": "llm-error-session",
    }

    with patch(
        "app.api.routes.chat.rag_pipeline.run",
        side_effect=RuntimeError("LLM unavailable"),
    ):
        response = api_client.post("/chat", json=payload)

    assert response.status_code == 500
