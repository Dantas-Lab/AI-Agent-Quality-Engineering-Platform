import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
def test_health_endpoint_returns_healthy_status(
    api_client: TestClient,
) -> None:
    response = api_client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
