import streamlit as st


def render_sidebar():

    st.sidebar.title("Navigation")

    st.sidebar.success("Project Status")

    st.sidebar.write("✅ FastAPI Running")

    st.sidebar.write("🚧 AI Module Coming Soon")

    st.sidebar.write("🚧 Kubernetes Collector Coming Soon")

    st.sidebar.write("🚧 Docker Collector Coming Soon")

    st.sidebar.write("🚧 Jenkins Collector Coming Soon")