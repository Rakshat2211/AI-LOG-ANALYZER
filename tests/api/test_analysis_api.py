from unittest.mock import patch


@patch(
    "backend.services.analysis_service.generate_ai_analysis"
)
def test_analysis_endpoint(

    mock_ai,

    client,
):

    mock_ai.return_value = (
        "Everything looks healthy."
    )

    response = client.get("/analysis")

    assert response.status_code == 200

    body = response.json()

    assert "analysis_context" in body

    assert "ai_summary" in body

    assert body["ai_summary"] == (
        "Everything looks healthy."
    )