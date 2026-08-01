import pandas as pd
import plotly.express as px
import streamlit as st


def render_level_pie(level_counts: dict):

    if not level_counts:
        st.info("No log levels available.")
        return

    df = pd.DataFrame(
        {
            "Level": list(level_counts.keys()),
            "Count": list(level_counts.values()),
        }
    )

    fig = px.pie(
        df,
        values="Count",
        names="Level",
        title="Log Level Distribution",
        hole=0.45,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_source_bar(source_counts: dict):

    if not source_counts:
        st.info("No source data available.")
        return

    df = pd.DataFrame(
        {
            "Source": list(source_counts.keys()),
            "Logs": list(source_counts.values()),
        }
    )

    fig = px.bar(
        df,
        x="Source",
        y="Logs",
        title="Logs by Source",
        text="Logs",
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_top_sources(source_counts: dict):

    if not source_counts:
        return

    df = pd.DataFrame(
        {
            "Source": list(source_counts.keys()),
            "Logs": list(source_counts.values()),
        }
    )

    df = df.sort_values(
        by="Logs",
        ascending=False,
    )

    st.subheader("Top Sources")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )