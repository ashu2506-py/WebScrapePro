import streamlit as st


def show_header():

    st.markdown(
        """
        <div class="dashboard-title">
            📈 WebScrapePro
        </div>

        <div class="dashboard-subtitle">

        Real-Time E-Commerce Price Intelligence Dashboard

        </div>

        <br>
        """,
        unsafe_allow_html=True
    )