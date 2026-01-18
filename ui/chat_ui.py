import streamlit as st


def render_chat(chat_history):
    for role, msg in chat_history:
        st.chat_message(role).write(msg)
