# 📘 Assignment: Persistent FastAPI Tasks with SQLite

## 🎯 Objective

Extend a FastAPI task API to store its data in a SQLite database instead of keeping tasks only in memory. Practice creating a table and using SQL queries to implement persistent CRUD operations.

## 📝 Tasks

### 🛠️ Create the SQLite Database

#### Description
Use the provided starter code to connect the API to a SQLite database. Create a `tasks` table when the application starts so the API can be launched repeatedly without losing the table structure.

To prepare the environment, save the starter code as `main.py`, install the API dependencies, and start the server:

```bash
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

#### Requirements
The completed program must:

- Create a SQLite database file named `tasks.db` when the application starts.
- Create a `tasks` table with columns for `id`, `title`, `description`, and `completed`.
- Give `id` an automatically generated unique value and require a title for every task.

### 🛠️ Save and List Tasks

#### Description
Replace the in-memory task storage with SQLite queries. Implement the API operations for creating a task and listing saved tasks.

#### Requirements
The completed program must:

- Implement `POST /tasks` to save a task and return its generated ID with the task data.
- Implement `GET /tasks` to return all saved tasks.
- Use SQL placeholders (`?`) to pass values into queries rather than building SQL with string formatting.
- Commit database changes so newly created tasks are saved.

### 🛠️ Read, Update, and Delete Saved Tasks

#### Description
Complete the CRUD operations by looking up, updating, and deleting tasks by ID. Then verify that saved data is still available after restarting the server.

#### Requirements
The completed program must:

- Implement `GET /tasks/{task_id}`, `PUT /tasks/{task_id}`, and `DELETE /tasks/{task_id}`.
- Return `404 Not Found` when a task ID does not exist.
- Return `204 No Content` after successfully deleting a task.
- Keep created and updated tasks available after the server is stopped and started again.
- Allow the routes to be tested through the interactive documentation at `http://127.0.0.1:8000/docs`.