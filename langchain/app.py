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
backend_url = st.text_input("FastAPI backend URL", value="http://localhost:8005/ask")
openai_api_key = st.text_input("OpenAI API Key (optional, overrides .env)", type="password")
question = st.text_input("Enter your question:")

if st.button("Ask") and question:
    try:
        payload = {"question": question}
        if openai_api_key:
            payload["openai_api_key"] = openai_api_key
        response = requests.post(backend_url, json=payload)
        if response.status_code == 200:
            st.success(f"AI Agent Response: {response.json().get('answer', 'No answer returned')}")
        else:
            st.error(f"Error from backend: {response.status_code}")
    except Exception as e:
        st.error(f"Request failed: {e}")

st.markdown("---")
st.header("Demonstration of Langchain Tutorial Code")
st.markdown("#### Langchain LLMChain Example")
st.code('''from langchain.llms import OpenAI\nfrom langchain.chains import LLMChain\nfrom langchain.prompts import PromptTemplate\n\nllm = OpenAI()\nprompt = PromptTemplate(input_variables=[\"question\"], template=\"Q: {question}\\nA:\")\nchain = LLMChain(llm=llm, prompt=prompt)\nresponse = chain.run(question=\"What is Langchain?\")\nprint(\"Langchain LLM Response:\", response)''', language='python')

st.markdown("#### RAG (Retrieval Augmented Generation) Example")
st.code('''from langchain.vectorstores import FAISS\nfrom langchain.embeddings import OpenAIEmbeddings\nfrom langchain.chains import RetrievalQA\n\ntexts = [\n    \"Langchain is a framework for developing applications powered by language models.\",\n    \"RAG stands for Retrieval Augmented Generation.\",\n    \"You can use Langchain with FastAPI and Streamlit.\"\n]\nembeddings = OpenAIEmbeddings()\nvectorstore = FAISS.from_texts(texts, embeddings)\nretriever = vectorstore.as_retriever()\nqa = RetrievalQA.from_chain_type(llm=llm, chain_type=\"stuff\", retriever=retriever)\nanswer = qa.run(\"What is RAG?\")\nprint(\"RAG Answer:\", answer)''', language='python')

st.info("To try the above, ensure your FastAPI backend is running and you have set your OpenAI API key.")
