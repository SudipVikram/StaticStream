import streamlit as st

from views import login
from views import create_post

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
        #st.toast('Welcome Superuser!', icon='✅')
        # dashboard for the Superuser
        #-----------
        # SIDEBAR
        #-----------
        with st.sidebar:
            # --- Session State Initialization ---
            if "current_page" not in st.session_state:
                st.session_state.current_page = "Insights"


            def set_page(page):
                st.session_state.current_page = page


            # --- Sidebar UI ---
            with st.sidebar:
                st.title("🚀 Static Stream Dashboard")
                st.caption(f"Logged in as: {st.session_state.get('role')}")
                st.divider()

                # --- Dashboard ---
                with st.expander("📊 Dashboard", expanded=(
                        st.session_state.current_page in ["Insights", "Traffic", "About"])):
                    if st.button("Insights", use_container_width=True): set_page("Insights")
                    if st.button("Analytics", use_container_width=True): set_page("Analytics")
                    if st.button("About", use_container_width=True): set_page("About")

                # --- Posts ---
                with st.expander("📝 Posts"):
                    if st.button("Create Post", use_container_width=True): set_page("Create Post")
                    if st.button("All Posts", use_container_width=True): set_page("All Posts")
                    if st.button("Update Post", use_container_width=True): set_page("Update Post")

                # --- Pages ---
                with st.expander("📄 Pages"):
                    if st.button("Generate Page", use_container_width=True): set_page("Generate Page")
                    if st.button("All Pages", use_container_width=True): set_page("All Pages")
                    if st.button("Update Page", use_container_width=True): set_page("Update Page")

                # --- Templates ---
                with st.expander("🎨 Templates"):
                    if st.button("View Templates", use_container_width=True): set_page("View Templates")
                    if st.button("Update Templates", use_container_width=True): set_page("Update Templates")

                # --- Settings ---
                with st.expander("⚙️ Settings"):
                    if st.button("User Settings", use_container_width=True): set_page("User Settings")
                    if st.button("Website Settings", use_container_width=True): set_page("Website Settings")

                if st.button("Logout"):
                    st.session_state.logged_in = False
                    st.rerun()

        #-------------
        # Page Route
        #-------------
        # --- Main Content Logic ---
        #st.header(f"Selection: {st.session_state.current_page}")
        if st.session_state.current_page == "Insights":
            st.title("Insights")
        elif st.session_state.current_page == "Analytics":
            st.title("Analytics")
            st.write("Coming soon...")
        elif st.session_state.current_page == "About":
            st.title("About")
            st.write("This CMS was written for the deployment of Beyond Apogee's website"
                     "by Sudip Vikram Adhikari. It is based on Streamlit. It is in github, "
                     "open for anyone to make it their own, tweak as they please, so enjoy!")
        elif st.session_state.current_page == "Create Post":
            create_post.render()


    elif st.session_state["role"] == "writer":
        st.write("Logged In as Writer")
    elif st.session_state["role"] == "editor":
        st.write("Logged In as Editor")