from datetime import datetime

import pandas as pd
import streamlit as st

from services.api import (
    create_log,
    get_backend_status,
    get_logs,
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

                st.success("Log Created Successfully")
                st.rerun()  # Refresh the page to show the new log

            else:

                st.error("Unable to create log")

    st.divider()

    st.header("Stored Logs")

    logs = get_logs()

    if logs:

        df = pd.DataFrame(logs)

        st.dataframe(
            df,
            use_container_width=True,
        )

    else:

        st.info("No Logs Found")