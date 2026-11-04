from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1
