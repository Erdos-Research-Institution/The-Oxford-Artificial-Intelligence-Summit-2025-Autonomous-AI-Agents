import streamlit as st
import requests

st.title("Langchain AI Agent Tutorial")
st.markdown("""
### Subtopics
- Langchain basics
- Langchain Memory, Tool usage
- RAG (Retrieval Augmented Generation)
- FastAPI backend (connect with Streamlit frontend)
""")

st.header("Ask the AI Agent (via FastAPI backend)")
backend_url = st.text_input("FastAPI backend URL", value="http://localhost:8000/ask")
question = st.text_input("Enter your question:")
if st.button("Ask") and question:
    try:
        response = requests.post(backend_url, json={"question": question})
        if response.status_code == 200:
            st.success(f"AI Agent Response: {response.json().get('answer', 'No answer returned')}")
        else:
            st.error(f"Error from backend: {response.status_code}")
    except Exception as e:
        st.error(f"Request failed: {e}")
