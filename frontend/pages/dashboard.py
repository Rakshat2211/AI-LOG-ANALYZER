import streamlit as st


def render_dashboard():

    st.title("🤖 Intelligent Log Analyzer")

    st.markdown(
        """
        Welcome to the AI Powered Intelligent Log Analysis Platform.

        This dashboard will allow you to:

        - Analyze Kubernetes Logs
        - Analyze Docker Logs
        - Analyze Jenkins Logs
        - Detect Anomalies
        - Perform AI Root Cause Analysis
        - Search Logs using AI
        """
    )

    st.divider()

    st.subheader("Project Progress")

    st.progress(15)

    st.info(
        "Milestone 1 - Project Foundation"
    )