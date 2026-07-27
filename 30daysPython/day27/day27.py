# Custom Middleware (Request Timer)

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    end = time.time()

    response.headers["X-Process-Time"] = str(end - start)

    return response


@app.get("/")
def home():
    return {"message": "Hello"}


# Dependency Injection with Classes

from fastapi import FastAPI, Depends

app = FastAPI()


class Database:

    def connect(self):
        return "Database Connected"


def get_db():
    return Database()


@app.get("/")
def home(db: Database = Depends(get_db)):
    return {"message": db.connect()}


# Global Configuration


#config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    admin_email: str = "admin@test.com"


settings = Settings()

#main.py

from fastapi import FastAPI
from config import settings

app = FastAPI(title=settings.app_name)


@app.get("/")
def home():
    return {"email": settings.admin_email}

# Custom Exception

from fastapi import FastAPI, HTTPException

app = FastAPI()


class StudentNotFound(Exception):
    pass


@app.exception_handler(StudentNotFound)
async def student_exception(request, exc):
    return {
        "message": "Student Not Found"
    }


@app.get("/{id}")
def get_student(id: int):

    if id != 1:
        raise StudentNotFound()

    return {"id": id}


# Streaming Response

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


def numbers():

    for i in range(1, 6):
        yield f"{i}\n"


@app.get("/")
def stream():
    return StreamingResponse(numbers())


# GZip Compression

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/")
def home():
    return {"message": "Compressed Response"}



# Generate UUID

import uuid
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def generate():

    return {
        "id": str(uuid.uuid4())
    }


# Custom Headers


from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def home(response: Response):

    response.headers["Developer"] = "Shruti"

    return {"message": "Header Added"}


# Enum Validation


from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class Department(str, Enum):
    IT = "IT"
    HR = "HR"
    SALES = "Sales"


@app.get("/{dept}")
def department(dept: Department):
    return {"Department": dept}

# UUID Path Parameter


from uuid import UUID
from fastapi import FastAPI

app = FastAPI()


@app.get("/{user_id}")
def user(user_id: UUID):
    return {
        "UUID": user_id
    }
