from unittest.mock import patch


@patch(
    "backend.api.collectors.CollectorManager"
)
def test_run_collectors(

    mock_manager,

    client,
):

    manager = mock_manager.return_value

    manager.collect_all_logs.return_value = 7

    response = client.post(
        "/collectors/run"
    )

    assert response.status_code == 200

    assert response.json() == {

        "message":
        "7 logs collected successfully."

    }