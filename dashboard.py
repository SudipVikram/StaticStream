import streamlit as st

from views import login

st.set_page_config(page_title="Static Stream CMS",layout="wide")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login handler
if not st.session_state.logged_in:
    login.render()
    st.stop()
else:
    st.write("Logged In")