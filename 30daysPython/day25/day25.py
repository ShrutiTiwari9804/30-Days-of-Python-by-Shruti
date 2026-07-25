# FILE UPLOADS

from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }


# FORM DATA

from fastapi import Form

@app.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return {"username": username}



# COOKIES- SET COOKIE

from fastapi import Response

@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="username", value="Shruti")
    return {"message": "Cookie set"}


# COOKIES- READ COOKIE


from fastapi import Cookie

@app.get("/get-cookie")
def get_cookie(username: str = Cookie(None)):
    return {"username": username}


# RESPONSE MODEL

class UserOut(BaseModel):
    id: int
    username: str

@app.get("/user/{id}", response_model=UserOut)
def get_user(id: int):
    return {
        "id": 1,
        "username": "Shruti",
        "password": "secret"
    }


# STATUS CODES

from fastapi import status

@app.post("/create", status_code=status.HTTP_201_CREATED)
def create():
    return {"message":"Created"}



# CUSTOM RESPONSE CLASSES- PLAIN TEST 

from fastapi.responses import PlainTextResponse

@app.get("/", response_class=PlainTextResponse)
def home():
    return "Hello"

# CUSTOM RESPONSE- HTML

from fastapi.responses import HTMLResponse

@app.get("/html", response_class=HTMLResponse)
def html():
    return "<h1>Hello</h1>"


# CUSTOM RESPONSE CLASSES- REDIRECT

from fastapi.responses import RedirectResponse

@app.get("/google")
def redirect():
    return RedirectResponse("https://google.com")

# BACKGROUND TASKS

from fastapi import BackgroundTasks

def send_email():
    print("Email Sent")

@app.get("/email")
def email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return {"message":"Sending Email"}

# MIDDLEWARE

from fastapi import Request

@app.middleware("http")
async def middleware(request: Request, call_next):

    print("Before Request")

    response = await call_next(request)

    print("After Request")

    return response



# CORS

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)



# ENVIRONMENT VARIABLES


pip install python-dotenv


DATABASE_URL=sqlite:///test.db
SECRET_KEY=mysecret

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DATABASE_URL"))


