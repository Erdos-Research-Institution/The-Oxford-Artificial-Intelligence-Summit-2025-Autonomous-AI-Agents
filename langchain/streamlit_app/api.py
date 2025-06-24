from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

app = FastAPI()

class Query(BaseModel):
    question: str

llm = OpenAI()
prompt = PromptTemplate(input_variables=["question"], template="Q: {question}\nA:")
chain = LLMChain(llm=llm, prompt=prompt)

@app.post("/ask")
def ask(query: Query):
    response = chain.run(question=query.question)
    return {"answer": response}
