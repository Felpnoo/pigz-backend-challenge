# Pigz Backend Challenge (To-Do List API)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**My implementation of the "Challenge 1" (To-Do List) from Orange Labs/Pigz.**

## 🎯 The Goal
The original challenge requests a task management system. I built a REST API where users can manage lists and tasks.

I chose **Python (FastAPI)** instead of the suggested PHP (Symfony) to demonstrate:
* **Performance:** High throughput with asynchronous endpoints.
* **Type Safety:** Data validation using **Pydantic V2**.
* **Reliability:** Automated tests with **Pytest**.

## 🏗 Architecture
The system uses a relational model (One-to-Many).
* **ToDoList:** The main container (e.g., "Work", "Groceries").
* **Task:** Items belonging to a list (e.g., "Email client", "Buy milk").

## 🛠 Tech Stack
* **Framework:** FastAPI
* **Database:** PostgreSQL (Production via Docker) / SQLite (Testing)
* **ORM:** SQLAlchemy 2.0
* **Infrastructure:** Docker Compose & NixOS Flakes

## 🚀 How to Run

### Option 1: Using Docker (Recommended)
This sets up the database and the API container automatically.

```bash
docker-compose up -d --build
```

The API will be available at: http://localhost:8000/docs

### Option 2: Local Development (NixOS/Linux)
If you want to run it manually:

Bash
# 1. Enter the environment

```bash
nix develop
```

# 2. Run the server
```bash
uvicorn app.main:app --reload
```
## 🧪 Testing

I included integration tests that use an in-memory database. This ensures the logic works without messing up the main database.


```bash
pytest
```

## 🔌 API Endpoints
Lists

*POST /lists/ - Create a new To-Do list.

*GET /lists/ - View all lists.

*DELETE /lists/{id} - Delete a list.

Tasks

*POST /lists/{id}/tasks/ - Add a task to a specific list.

*PATCH /tasks/{id}/complete - Mark a task as done.
```
>Implemented by Felipe Silva.
