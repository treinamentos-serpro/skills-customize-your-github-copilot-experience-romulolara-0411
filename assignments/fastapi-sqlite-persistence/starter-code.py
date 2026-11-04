from contextlib import closing
import sqlite3

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

DATABASE_PATH = "tasks.db"
app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        # TODO: Create the tasks table with id, title, description, and completed columns.
        pass


initialize_database()


def row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"],
        completed=bool(row["completed"]),
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Query all tasks and convert each row with row_to_task().
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: Insert the task using SQL placeholders, commit, and return the saved task.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Query by ID and raise HTTPException with status 404 when missing.
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    # TODO: Update by ID, commit, and return 404 when no task was updated.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete by ID, commit, and return 404 when no task was deleted.
    raise NotImplementedError