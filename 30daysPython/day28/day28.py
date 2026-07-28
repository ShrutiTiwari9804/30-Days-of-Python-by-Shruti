
# Decimal for Prices

from uuid import UUID
from fastapi import FastAPI

app = FastAPI()


@app.get("/{user_id}")
def user(user_id: UUID):
    return {
        "UUID": user_id
    }



# Multiple Routers

# users.py


from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.get("/")
def users():
    return ["A", "B"]


# main.py


from fastapi import FastAPI
from users import router

app = FastAPI()

app.include_router(router)


# API Tags


from fastapi import FastAPI

app = FastAPI()


@app.get("/users", tags=["Users"])
def users():
    return {"message": "Users"}


# Path Operation Metadata


from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/",
    summary="Home API",
    description="Returns welcome message"
)
def home():
    return {"message": "Welcome"}


# Hide Endpoint


from fastapi import FastAPI

app = FastAPI()


@app.get("/secret", include_in_schema=False)
def secret():
    return {"message": "Hidden"}



# Health Check Endpoint


from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# API Root Endpoint


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Welcome to Student Management API",
        "version": "1.0"
    }


