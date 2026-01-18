import streamlit as st
from dotenv import load_dotenv

from core.loader import load_pdfs
from core.splitter import split_documents
from core.vectorstore import create_vectorstore
from core.rag_chain import build_rag_chain
from ui.chat_ui import render_chat

load_dotenv()

st.set_page_config(page_title="Interact", layout="wide")

# ------------------ SESSION STATE ------------------
st.session_state.setdefault("vectorstore", None)
st.session_state.setdefault("chat_history", [])

st.title("Interact with your Docs")

# ------------------ FILE UPLOAD ------------------
uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.sidebar.button("Process Documents"):
    docs = load_pdfs(uploaded_files)
    chunks = split_documents(docs)
    st.session_state.vectorstore = create_vectorstore(chunks)
    st.success("Documents processed!")

# ------------------ CHAT ------------------
if st.session_state.vectorstore:

    retriever = st.session_state.vectorstore.as_retriever()
    chain = build_rag_chain(retriever)

    user_input = st.chat_input("Ask a question...")

    if user_input:
        response = chain.invoke(user_input)

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", response))

    render_chat(st.session_state.chat_history)

else:
    st.info("<---- Upload documents to begin")
