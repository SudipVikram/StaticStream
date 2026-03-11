import streamlit as st
from services.auth_service import verify_user

def render():
    st.title("Static Stream CMS Login")

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        if verify_user(username, password):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username and password")