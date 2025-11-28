# rag_agent_app/backend/vectorstore.py

import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import API keys from .env
from backend.config import PINECONE_API_KEY, PINECONE_INDEX_NAME

# Set environment
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Embeddings = 384 dimensions
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Use .env index name
INDEX_NAME = PINECONE_INDEX_NAME

# --- Ensure Pinecone index exists ---
def ensure_index():
    if INDEX_NAME not in pc.list_indexes().names():
        print(f"Creating Pinecone index {INDEX_NAME} ...")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
        print("Index created.")

# --- RAG Retriever ---
def get_retriever():
    ensure_index()

    vectorstore = PineconeVectorStore(
        index=pc.Index(INDEX_NAME),
        embedding=embeddings
    )
    return vectorstore.as_retriever()


# --- Document Upload ---
def add_document_to_vectorstore(text_content: str):
    ensure_index()

    if not text_content:
        raise ValueError("Document content cannot be empty.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )

    documents = text_splitter.create_documents([text_content])
    print(f"Split into {len(documents)} chunks")

    vectorstore = PineconeVectorStore(
        index=pc.Index(INDEX_NAME),
        embedding=embeddings
    )

    vectorstore.add_documents(documents)
    print(f"Successfully added {len(documents)} chunks to {INDEX_NAME}")
