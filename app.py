from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"message": "Welcome to UniAssist!"}

@app.post("/chat/")
def chat_with_bot(query: QueryRequest):
    # You will replace this with real response from LLM
    return {"response": f"You said: {query.user_input}"}
