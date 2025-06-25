from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Allow CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str
    openai_api_key: str = None

@app.post("/ask")
async def ask_agent(req: QuestionRequest):
    question = req.question
    openai_api_key = req.openai_api_key or os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return {"answer": "Error: OpenAI API key not provided."}
    os.environ["OPENAI_API_KEY"] = openai_api_key
    # Setup Langchain objects (simple demo)
    llm = OpenAI()
    prompt = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")
    chain = LLMChain(llm=llm, prompt=prompt)
    # RAG setup (simple demo)
    texts = [
        "Langchain is a framework for developing applications powered by language models.",
        "RAG stands for Retrieval Augmented Generation.",
        "You can use Langchain with FastAPI and Streamlit."
    ]
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts, embeddings)
    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    # Use RAG for demo; fallback to LLMChain if needed
    try:
        answer = qa.run(question)
    except Exception:
        answer = chain.run(question=question)
    return {"answer": answer}
