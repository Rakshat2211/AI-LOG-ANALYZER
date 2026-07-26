from datetime import datetime

from backend.schemas.log import LogCreate


def test_add_log(client):
    """
    Verify POST /logs
    creates a new log.
    """

    payload = {

        "timestamp": datetime.now().isoformat(),

        "source": "Dummy",

        "level": "INFO",

        "message": "Application Started",
    }

    response = client.post(

        "/logs/",

        json=payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert body["source"] == "Dummy"

    assert body["level"] == "INFO"

    assert body["message"] == "Application Started"


def test_fetch_logs_empty(client):
    """
    Empty database
    should return [].
    """

    response = client.get("/logs/")

    assert response.status_code == 200

    assert response.json() == []


def test_fetch_logs(client):

    payload = {

        "timestamp": datetime.now().isoformat(),

        "source": "Docker",

        "level": "ERROR",

        "message": "Container Failed",
    }

    client.post(

        "/logs/",

        json=payload,
    )

    response = client.get("/logs/")

    assert response.status_code == 200

    logs = response.json()

    assert len(logs) == 1

    assert logs[0]["source"] == "Docker"