import streamlit as st

def reset(page):
    if 'last_page' not in st.session_state:
        st.session_state.last_page = page
    if st.session_state.last_page != page:
        st.session_state.clear()
        st.session_state.last_page = page