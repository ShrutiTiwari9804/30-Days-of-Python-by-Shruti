# LOGGING

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application Started")


# PAGINATION

@app.get("/products")
def products(skip:int=0, limit:int=10):
    return data[skip:skip+limit]

# FILTERING


@app.get("/products")
def products(category:str=None):

    if category:
        return [i for i in data if i["category"]==category]

    return data


# SORTING


@app.get("/sort")
def sort():

    return sorted(data,key=lambda x:x["price"])


# EXCEPTION HANDLERS

from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)}
    )



# LIFESPAN EVENTS


from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")
    yield
    print("Application Closed")

app = FastAPI(lifespan=lifespan)



# API Versioning

from fastapi import APIRouter

v1 = APIRouter(prefix="/api/v1")

@v1.get("/users")
def users():
    return {"version":"v1"}

app.include_router(v1)



# MOUNTING STATIC FILES


from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")



# TEMPLATES ( JINJA2 )

pip install jinja2

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


# TESTING FASTAPI

from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

# WEBSOCKETS

from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")


