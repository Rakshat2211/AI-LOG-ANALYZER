import requests

from config import BACKEND_URL


def get_backend_status():

    try:

        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=5,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:

        return None


def create_log(data):

    try:

        response = requests.post(
            f"{BACKEND_URL}/logs",
            json=data,
            timeout=5,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:

        return None


def get_logs():

    try:

        response = requests.get(
            f"{BACKEND_URL}/logs",
            timeout=5,
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException:

        return []