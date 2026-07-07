import requests
import streamlit as st


BACKEND_URL = "http://127.0.0.1:8000"


def get_backend_status():
    """
    Calls the FastAPI health endpoint.

    Returns:
        dict | None
    """

    try:

        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=5,
        )

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.RequestException:
        return None

    return None


def render_dashboard():

    st.title("🤖 Intelligent Log Analyzer")

    st.write(
        "AI Powered Intelligent Log Analysis Platform"
    )

    st.divider()

    st.subheader("Backend Status")

    backend = get_backend_status()

    if backend:

        st.success("Backend Connected")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Application",
                backend["application"],
            )

            st.metric(
                "Environment",
                backend["environment"],
            )

        with col2:

            st.metric(
                "Status",
                backend["status"],
            )

            st.metric(
                "Version",
                backend["version"],
            )

    else:

        st.error("Backend is Offline")

    st.divider()

    st.info(
        "Milestone 1 - Part 4\n\nFrontend is now communicating with the FastAPI backend."
    )