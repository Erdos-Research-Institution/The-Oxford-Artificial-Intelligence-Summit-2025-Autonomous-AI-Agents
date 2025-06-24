"""
Langchain AI Agent Tutorial
Subtopics:
- Langchain basics
- Langchain Memory, Tool usage
- RAG (Retrieval Augmented Generation)
- FastAPI backend (connect with Streamlit frontend)
"""

# Langchain basics
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = OpenAI()
prompt = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")
chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run(question="What is Langchain?")
print("Langchain LLM Response:", response)

# Memory and Tool usage
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
memory.save_context({"input": "Hello"}, {"output": "Hi!"})
print("Memory Buffer:", memory.buffer)

# RAG (Retrieval Augmented Generation)
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import numpy as np

# Dummy RAG example (real use would require documents and embeddings)
# vectorstore = FAISS.from_texts(["Langchain is cool!"], OpenAIEmbeddings())
# qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
# answer = qa.run("What is Langchain?")
# print("RAG Answer:", answer)

# Lightweight RAG (Retrieval Augmented Generation) Example
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

# Create a simple document list
texts = ["Langchain is a framework for developing applications powered by language models.",
         "RAG stands for Retrieval Augmented Generation.",
         "You can use Langchain with FastAPI and Streamlit."]

# Use OpenAIEmbeddings (requires OPENAI_API_KEY env variable)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)
retriever = vectorstore.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

answer = qa.run("What is RAG?")
print("RAG Answer:", answer)

# FastAPI backend (see api.py for implementation)
