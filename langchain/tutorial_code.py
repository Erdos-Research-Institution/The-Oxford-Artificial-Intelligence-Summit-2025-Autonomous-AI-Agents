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
import os

# RAG (Retrieval Augmented Generation)
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import numpy as np
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()

os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")

llm = OpenAI()
prompt = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")
chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run(question="What is Langchain?")
print("Langchain LLM Response:", response)

# Memory and Tool usage

memory = ConversationBufferMemory()
memory.save_context({"input": "Hello"}, {"output": "Hi!"})
print("Memory Buffer:", memory.buffer)



# Create a simple document list
texts = ["Langchain is a framework for developing applications powered by language models.",
         "RAG stands for Retrieval Augmented Generation.",
         "You can use Langchain with FastAPI and Streamlit."]

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)
retriever = vectorstore.as_retriever()
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

answer = qa.run("What is RAG?")
print("RAG Answer:", answer)

# FastAPI backend (see api.py for implementation)
