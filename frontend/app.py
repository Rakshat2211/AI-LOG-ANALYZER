import streamlit as st

from config import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from components.sidebar import render_sidebar

from pages.dashboard import render_dashboard


st.set_page_config(

    page_title=APP_TITLE,

    page_icon=PAGE_ICON,

    layout=LAYOUT,

)


render_sidebar()

render_dashboard()