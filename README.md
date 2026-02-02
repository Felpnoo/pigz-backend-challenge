# 🍕 Pigz Backend Challenge (Python Edition)

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**A modern, high-performance implementation of the Pigz Backend Challenge using Python, FastAPI, and Docker.**

## 🎯 The Approach
While the original challenge suggests PHP/Symfony, this solution leverages **FastAPI** to demonstrate:
* **Performance:** Asynchronous capabilities and high throughput.
* **Type Safety:** Robust validation using **Pydantic V2**.
* **Clean Architecture:** Separation of concerns (Models, Schemas, Routers).
* **Testing:** Automated integration tests with **Pytest** and SQLite in-memory.

## 🛠 Tech Stack
* **Framework:** FastAPI
* **Database:** PostgreSQL (Production) / SQLite (Testing)
* **ORM:** SQLAlchemy 2.0
* **Infrastructure:** Docker Compose & NixOS Flakes

## 🚀 How to Run

### Option A: Using Docker (Recommended)
```bash
# Start Database
docker-compose up -d

# Run API
uvicorn app.main:app --reload
```

# Option B: Running Tests
```bash
pytest
```
Implemented by Felipe Silva to demonstrate backend proficiency.
