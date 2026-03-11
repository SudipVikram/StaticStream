import streamlit as st
from datetime import datetime
from database.db import get_cursor

def render():
    cursor, conn = get_cursor()

    st.title("Create New Post")

    with st.form("new_post_submission"):
        title = st.text_input("Title")
        slug = st.text_input("Slug")
        meta = st.text_input("Meta")
        excerpt = st.text_area("Excerpt")
        content = st.text_area("Content")
        publish = st.checkbox("Publish")

        if st.form_submit_button("Save"):
            cursor.execute(
                """
                INSERT INTO posts(title, slug, meta, content, excerpt, created_at, published)
                VALUES(?,?,?,?,?,?,?)
                """,
                (
                    title,
                    slug,
                    meta,
                    content,
                    excerpt,
                    datetime.now().isoformat(),
                    int(publish)
                )
            )
            conn.commit()
            st.success("Post Saved")


