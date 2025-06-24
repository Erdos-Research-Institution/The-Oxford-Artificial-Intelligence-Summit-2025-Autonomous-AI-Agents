import streamlit as st
import requests
import os
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

st.title("Langchain AI Agent Tutorial")
st.markdown("""
### Subtopics
- Langchain basics
- Langchain Memory, Tool usage
- RAG (Retrieval Augmented Generation)
- FastAPI backend (connect with Streamlit frontend)
""")

st.header("Ask the AI Agent (via FastAPI backend)")
question = st.text_input("Enter your question:")
if st.button("Ask") and question:
    try:
        response = requests.post("http://localhost:8000/ask", json={"question": question})
        if response.status_code == 200:
            st.write("**Answer:**", response.json()["answer"])
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Could not connect to FastAPI backend: {e}")

st.header("RAG Example (Local, Lightweight)")
if os.environ.get("OPENAI_API_KEY"):
    texts = [
        "Langchain is a framework for developing applications powered by language models.",
        "RAG stands for Retrieval Augmented Generation.",
        "You can use Langchain with FastAPI and Streamlit."
    ]
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts, embeddings)
    retriever = vectorstore.as_retriever()
    llm = OpenAI()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    rag_question = st.text_input("Ask a RAG question:", key="rag")
    if st.button("Ask RAG") and rag_question:
        rag_answer = qa.run(rag_question)
        st.write("**RAG Answer:**", rag_answer)
else:
    st.info("Set your OPENAI_API_KEY environment variable to try the RAG example.")

st.header("Langchain Memory Example")
st.write("See tutorial_code.py for memory and RAG examples.")

st.header("Industry Use Case")
st.markdown("""
Langchain is used in industry for building advanced AI agents that can remember conversations, use tools, and retrieve information from large document sets (RAG). Connecting a FastAPI backend to Streamlit enables scalable, production-ready AI applications.
""")
