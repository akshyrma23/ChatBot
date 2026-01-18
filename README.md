
RAG-Based Document Question Answering System

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload documents and ask questions about them using an LLM.
Built using Streamlit, LangChain, OpenAI, and FAISS.  

## 👤 Author

This project was created by **Akshay** for **learning and educational purposes**.

The goal of this project is to understand and implement:
- Retrieval-Augmented Generation (RAG)
- LangChain architecture
- Vector databases (FAISS)
- LLM-based question answering
- Streamlit-based applications

This project is not intended for production use but as a hands-on learning implementation.


Architecture Overview
User
  │
  ▼
Streamlit UI
  │
  ▼
Document Loader
  │
  ▼
Text Splitter
  │
  ▼
Embedding Generator
  │
  ▼
FAISS Vector Store
  │
  ▼
Retriever
  │
  ▼
LLM (GPT-4o-mini)
  │
  ▼
Answer Display



1️⃣ Clone the Repository
git clone https://github.com/akshyrma23/ChatBot

cd rag_chatbot

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key

▶️ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501

