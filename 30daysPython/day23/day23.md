# 🚀 FastAPI Basics

A beginner-friendly guide to learning **FastAPI**, one of the fastest and most modern Python web frameworks for building APIs.

---

# 📖 What is FastAPI?

FastAPI is a modern Python framework used for creating **REST APIs** quickly and efficiently.

It is built on:

* **Starlette** – Handles web requests and responses.
* **Pydantic** – Validates and serializes data.

FastAPI is widely used because it is:

* ⚡ Extremely Fast
* 📚 Easy to Learn
* ✅ Automatic Data Validation
* 📄 Automatic API Documentation
* 🔄 Supports Asynchronous Programming
* 🏢 Used in Real-World Production Applications

---

# 📦 Installation

## Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

---

# ▶ Running the Application

If your file is named **main.py**, run:

```bash
uvicorn main:app --reload
```

### Explanation

* **main** → Python filename (`main.py`)
* **app** → FastAPI application object
* **--reload** → Automatically reloads the server whenever you save changes

---

# 🌐 Open in Browser

Application

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 📁 Basic Project Structure

```
FastAPI_Project/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

# 🏗 Creating the FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()
```

The `FastAPI()` object creates the web application. All routes are attached to this object.

---

# 📌 Path Operations

A path operation connects a URL to a Python function.

Example:

```python
@app.get("/")
def home():
    return {"message": "Welcome"}
```

When someone visits:

```
GET /
```

FastAPI executes the `home()` function and returns a JSON response.

---

# 🌍 HTTP Methods

| Method | Purpose              |
| ------ | -------------------- |
| GET    | Retrieve data        |
| POST   | Create new data      |
| PUT    | Update complete data |
| PATCH  | Update partial data  |
| DELETE | Remove data          |

---

# 📂 Path Parameters

Path parameters are values passed directly in the URL.

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Request:

```
/users/10
```

Response:

```json
{
    "user_id": 10
}
```

---

# 🔍 Query Parameters

Query parameters appear after the `?` in the URL.

Example:

```python
@app.get("/search")
def search(item: str):
    return {"item": item}
```

Request:

```
/search?item=laptop
```

Response:

```json
{
    "item": "laptop"
}
```

---

# ⭐ Optional Query Parameters

Assigning a default value makes a query parameter optional.

```python
@app.get("/books")
def books(category: str = "Programming"):
    return {"category": category}
```

Examples:

```
/books
```

or

```
/books?category=Python
```

---

# 📤 Returning JSON

FastAPI automatically converts Python dictionaries into JSON.

Python

```python
return {"name": "Shruti"}
```

JSON Response

```json
{
    "name": "Shruti"
}
```

---

# 📝 Type Hints

FastAPI uses Python type hints for automatic validation.

Example:

```python
@app.get("/square/{number}")
def square(number: int):
    return {"square": number * number}
```

If a string is passed instead of an integer, FastAPI automatically returns a validation error.

---

# 📚 Automatic API Documentation

FastAPI generates API documentation automatically.

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

These pages allow you to test your API without writing frontend code.

---

# 💡 Advantages of FastAPI

* High Performance
* Easy Syntax
* Automatic API Documentation
* Built-in Request Validation
* JSON Serialization
* Excellent IDE Support
* Async Support
* Production Ready

---

# 📖 Basic FastAPI Concepts Covered

* FastAPI Introduction
* Installing FastAPI
* Creating the FastAPI Application
* Running the Server
* Path Operations
* GET Requests
* HTTP Methods
* Returning JSON Responses
* Path Parameters
* Query Parameters
* Optional Query Parameters
* Type Hints
* Automatic Validation
* Swagger Documentation
* ReDoc Documentation

---

# 🎯 Sample API Endpoints

| Endpoint                | Method | Description              |
| ----------------------- | ------ | ------------------------ |
| `/`                     | GET    | Home Page                |
| `/about`                | GET    | About Page               |
| `/user/{id}`            | GET    | Get User by ID           |
| `/student/{name}/{age}` | GET    | Multiple Path Parameters |
| `/search?item=laptop`   | GET    | Query Parameter Example  |
| `/books`                | GET    | Optional Query Parameter |

---

# 🚀 Next Topics

The next concepts to learn in FastAPI include:

* POST Requests
* Request Body
* Pydantic Models
* CRUD Operations
* Response Models
* Status Codes
* Path & Query Validation
* Dependency Injection
* APIRouter
* Database Integration (SQLAlchemy)
* Authentication & Authorization (JWT)
* File Uploads
* Background Tasks
* Middleware
* Exception Handling
* Testing APIs
* Deployment

---

# 📌 Learning Goal

This project is the starting point of my FastAPI backend development journey. It covers the core fundamentals required to understand how APIs work before moving on to database integration, authentication, and real-world backend projects.
