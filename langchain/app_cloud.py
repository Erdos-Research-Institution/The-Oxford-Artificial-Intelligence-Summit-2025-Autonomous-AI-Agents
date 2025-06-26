import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os

st.title("Langchain AI Agent Tutorial (Cloud Version)")
st.markdown("""
### Subtopics
- Langchain basics
- Langchain Memory, Tool usage
- RAG (Retrieval Augmented Generation)
""")

openai_api_key = st.text_input("OpenAI API Key", type="password")
question = st.text_input("Enter your question:")

if st.button("Ask") and question:
    if not openai_api_key:
        st.error("Please enter your OpenAI API Key.")
    else:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        try:
            # LLMChain example
            llm = OpenAI()
            prompt = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")
            chain = LLMChain(llm=llm, prompt=prompt)

            # RAG setup
            texts = [
                "Langchain is a framework for developing applications powered by language models.",
                "RAG stands for Retrieval Augmented Generation.",
                "You can use Langchain with FastAPI and Streamlit."
            ]
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_texts(texts, embeddings)
            retriever = vectorstore.as_retriever()
            qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

            # Try RAG, fallback to LLMChain
            try:
                answer = qa.run(question)
            except Exception:
                answer = chain.run(question=question)
            st.success(f"AI Agent Response: {answer}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.header("Demonstration of Langchain Tutorial Code")
st.markdown("#### Langchain LLMChain Example")
st.code('''from langchain.llms import OpenAI\nfrom langchain.chains import LLMChain\nfrom langchain.prompts import PromptTemplate\n\nllm = OpenAI()\nprompt = PromptTemplate(input_variables=[\"question\"], template=\"Q: {question}\\nA:\")\nchain = LLMChain(llm=llm, prompt=prompt)\nresponse = chain.run(question=\"What is Langchain?\")\nprint(\"Langchain LLM Response:\", response)''', language='python')

st.markdown("#### RAG (Retrieval Augmented Generation) Example")
st.code('''from langchain.vectorstores import FAISS\nfrom langchain.embeddings import OpenAIEmbeddings\nfrom langchain.chains import RetrievalQA\n\ntexts = [\n    \"Langchain is a framework for developing applications powered by language models.\",\n    \"RAG stands for Retrieval Augmented Generation.\",\n    \"You can use Langchain with FastAPI and Streamlit.\"\n]\nembeddings = OpenAIEmbeddings()\nvectorstore = FAISS.from_texts(texts, embeddings)\nretriever = vectorstore.as_retriever()\nqa = RetrievalQA.from_chain_type(llm=llm, chain_type=\"stuff\", retriever=retriever)\nanswer = qa.run(\"What is RAG?\")\nprint(\"RAG Answer:\", answer)''', language='python')

st.info("To try the above, ensure you have set your OpenAI API key.")
