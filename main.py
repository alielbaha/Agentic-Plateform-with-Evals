from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title = "Agentic Plateform API", version = "O.1.O")

class TaskRequest(BaseModel):
    question : str = Field(min_length = 1, max_length = 2000) 

class TaskResponse(BaseModel):
    question : str
    answer : str
    agents_used : list[str]


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask", response_model = TaskResponse)
async def ask(request: TaskRequest):
    return TaskResponse(
        question = request.question,
        answer = "agent not avalable yet",
        agents_used = []
    )