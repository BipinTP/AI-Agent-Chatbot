# 📚 AI-Powered PDF Question-Answering System

An intelligent **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDFs, index their content, and ask questions about them with accurate AI-generated responses.

This end-to-end system uses **FastAPI, LangGraph, Pinecone, Groq LLM, and Streamlit**.

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Pinecone](https://img.shields.io/badge/VectorDB-Pinecone-yellow)
![RAG](https://img.shields.io/badge/AI-RAG%20App-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Features

### 📄 Upload PDF Documents  
- Upload one or more PDF files through the Streamlit UI  
- Extracts and processes text from PDFs using `PyPDFLoader`

### 🔍 Smart Text Chunking + Embeddings  
- Cleans and splits long documents into manageable chunks  
- Uses **HuggingFace embeddings** to convert text into vectors  

### 🗂️ Pinecone Vector Database  
- Stores embedded chunks in **Pinecone**  
- Enables fast **similarity search** for relevant context  

### 🤖 RAG-Based AI Assistant  
- Combines **retrieved PDF chunks + LLM** for accurate responses  
- Handles follow-up questions using chat history  

### 🌐 Optional Web Search (Tavily)  
- Uses **Tavily API** for real-time web information  
- Falls back to web search when PDF context is insufficient  

### 🔁 LangGraph Agent Workflow  
- Built with **LangGraph** to orchestrate the workflow  
- Routes between:
  - RAG over PDFs  
  - Web Search  
  - Direct LLM Answering  

### 💬 Interactive Chat UI (Streamlit)  
- Simple, clean chat interface  
- Shows **chat history** and **workflow trace** (what the agent did step-by-step)

---

## 🧠 Tech Stack

### Backend

- ⚙️ **FastAPI** – REST API backend  
- 🧩 **LangGraph** – Agent workflow & routing logic  
- 🧠 **Groq LLMs** – Fast and efficient LLM inference  
- 🗂️ **Pinecone** – Vector database for document retrieval  
- 🔡 **HuggingFace Embeddings** – Text embedding models  
- 🌐 **Tavily Web Search** – Optional external knowledge  
- 📄 **PyPDFLoader** – PDF text extraction  

### Frontend

- 🖥️ **Streamlit** – Web UI for chat and file upload  
- 🔗 **Requests** – Communication with FastAPI backend  

---

## 📦 Project Structure

```bash
rag_agent_app/
│── backend/
│   ├── main.py             # FastAPI entrypoint
│   ├── agent.py            # LangGraph agent logic
│   ├── config.py           # Settings & environment config
│   ├── vectorstore.py      # Pinecone vector store utilities
│
│── frontend/
│   ├── app.py              # Streamlit main app
│   ├── backend_api.py      # API client for FastAPI
│   ├── session_manager.py  # Session & chat history handling
│   ├── ui_components.py    # Reusable Streamlit UI components
│
│── .env                    # Environment variables (not committed)
│── README.md               # Project documentation

🛠️ Installation & Setup

1️⃣ Clone the repo
git clone https://github.com/your-username/ai-agent-chatbot
cd ai-agent-chatbot

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your API keys to .env
PINECONE_API_KEY=your_key
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key

5️⃣ Run backend (FastAPI)
cd backend
uvicorn main:app --reload

6️⃣ Run frontend (Streamlit)
cd frontend
streamlit run app.py
