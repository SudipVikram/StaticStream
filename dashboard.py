import streamlit as st

from views import login
from services.auth_service import get_role

st.set_page_config(page_title="Static Stream CMS",layout="wide")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login handler
if not st.session_state.logged_in:
    login.render()
    st.stop()
else:
    # logged into the database
    # checking user roles
    if st.session_state["role"] == "superuser":
        st.write("Logged In as Superuser")
    elif st.session_state["role"] == "writer":
        st.write("Logged In as Writer")
    elif st.session_state["role"] == "editor":
        st.write("Logged In as Editor")