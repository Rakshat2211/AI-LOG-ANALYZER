from datetime import datetime
import time
import pandas as pd
import streamlit as st

from services.api import (
    create_log,
    get_backend_status,
    get_logs,
    get_analysis,
    get_ai_analysis,
)

from components.charts import (
    render_level_pie,
    render_source_bar,
    render_top_sources,
)

def render_dashboard():

    st.title("🤖 Intelligent Log Analyzer")

    st.divider()

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

        st.error("Backend Offline")

        return

    st.divider()

# ----------------------------------
# Load Dashboard Analysis
# ----------------------------------

    if "analysis" not in st.session_state:

        start = time.time()

        st.session_state.analysis = get_analysis()

        st.session_state.analysis_time = (
            time.time() - start
        )

    if "ai_summary" not in st.session_state:

        st.session_state.ai_summary = None

    analysis = st.session_state.analysis

    if analysis is None:

        st.error("Unable to load dashboard data.")

        return

    refresh_col1, refresh_col2 = st.columns([1, 5])

    with refresh_col1:

        if st.button(
            "🔄 Refresh Dashboard"
        ):

            with st.spinner(
                "Refreshing dashboard..."
            ):

                start = time.time()

                st.session_state.analysis = get_analysis()

                st.session_state.analysis_time = (
                    time.time() - start
                )

                # Force AI regeneration
                st.session_state.ai_summary = None

            st.rerun()

    if analysis:

        st.header("📊 System Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Logs",
                analysis["total_logs"],
            )

        with col2:

            st.metric(
                "INFO",
                analysis["info_logs"],
            )

        with col3:

            st.metric(
                "WARNING",
                analysis["warning_logs"],
            )

        with col4:

            st.metric(
                "ERROR",
                analysis["error_logs"],
            )

        st.divider()
    
    st.header("📈 Log Analytics")

    left, right = st.columns(2)

    with left:

        render_level_pie(
            {
                "INFO": analysis["info_logs"],
                "WARNING": analysis["warning_logs"],
                "ERROR": analysis["error_logs"],
            }
        )

    with right:

        render_source_bar(
            analysis["logs_by_source"]
        )

    st.divider()

    render_top_sources(
        analysis["logs_by_source"]
    )

    st.header("⚠ Detected Anomalies")

    if analysis["anomalies"]:

        for anomaly in analysis["anomalies"]:

            st.warning(anomaly)

    else:

        st.success("No anomalies detected.")
    
    st.header("🤖 AI Analysis")

    if st.session_state.ai_summary is None:

        with st.spinner(
            "Generating AI Analysis..."
        ):

            ai_response = get_ai_analysis()

            if ai_response:

                st.session_state.ai_summary = (
                    ai_response["ai_summary"]
                )

    if st.session_state.ai_summary:

        st.info(
            st.session_state.ai_summary
        )

    else:

        st.warning(
            "AI analysis is currently unavailable."
        )

    st.header("Create New Log")

    with st.form("log_form"):

        timestamp = st.datetime_input(
            "Timestamp",
            datetime.now(),
        )

        source = st.selectbox(

            "Source",

            [

                "Kubernetes",

                "Docker",

                "Jenkins",

            ],

        )

        level = st.selectbox(

            "Level",

            [

                "INFO",

                "WARNING",

                "ERROR",

                "CRITICAL",

            ],

        )

        message = st.text_area("Message")

        submitted = st.form_submit_button("Create Log")

        if submitted:

            payload = {

                "timestamp": timestamp.isoformat(),

                "source": source,

                "level": level,

                "message": message,

            }

            result = create_log(payload)

            if result:

                st.success(
                    "Log Created Successfully"
                )

                if "analysis" in st.session_state:

                    del st.session_state.analysis

                if "analysis_time" in st.session_state:

                    del st.session_state.analysis_time

                if "ai_summary" in st.session_state:

                    del st.session_state.ai_summary

                st.rerun()

            else:

                st.error("Unable to create log")

    st.divider()

    st.header("Stored Logs")

    logs = analysis["logs"]

    if logs:

        df = pd.DataFrame(logs)

        st.dataframe(
            df,
            use_container_width=True,
        )

    else:

        st.info("No Logs Found")