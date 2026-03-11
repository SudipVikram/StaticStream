import streamlit as st
from services.auth_service import verify_user,get_role

def render():
    st.title("Static Stream CMS Login")

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        if verify_user(username, password):
            st.session_state.logged_in = True
            user_role = get_role(username)
            st.session_state["role"] = user_role[0]
            st.rerun()
        else:
            st.error("Invalid username and password")