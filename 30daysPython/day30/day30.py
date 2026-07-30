# Idempotent Methods
"""

 Method  Idempotent   
 ------  ------------ 
 GET      Yes        
 PUT      Yes        
 DELETE   Yes        
 POST     No         
 PATCH    Usually No 

 """

#  Stateless APIs

GET /profile
Authorization: Bearer JWT_TOKEN

# JSON

{
    "id":1,
    "name":"Alice",
    "city":"Pune"
}


# REST Naming Conventions

GET /students
GET /students/5
POST /students
PUT /students/5
DELETE /students/5


# Complete CRUD Example

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.post("/students")
def create(student: Student):
    students.append(student)
    return {"message": "Student Added", "student": student}

@app.get("/students")
def read():
    return students

@app.get("/students/{student_id}")
def read_one(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"message": "Student Not Found"}

@app.put("/students/{student_id}")
def update(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student Updated", "student": updated_student}
    return {"message": "Student Not Found"}

@app.delete("/students/{student_id}")
def delete(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {"message": "Student Deleted"}
    return {"message": "Student Not Found"}

# Authentication (JWT)

from fastapi import Depends

@app.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return current_user

# Authorization

if current_user.role != "admin":
    raise HTTPException(status_code=403)

# Pagination

@app.get("/students")
def students(skip: int = 0, limit: int = 10):
    return data[skip:skip+limit]

# Filtering 

@app.get("/students")
def students(city: str = None):

    if city:
        return [i for i in data if i["city"] == city]

    return data

# Sorting

@app.get("/students")
def students():

    return sorted(data, key=lambda x: x["name"])

# Searching

@app.get("/students")
def search(name: str):

    return [i for i in data if name.lower() in i["name"].lower()]

# API Versioning

/api/v1/students

/api/v2/students


from fastapi import APIRouter

v1 = APIRouter(prefix="/api/v1")

@v1.get("/students")
def students():
    return {"version": "v1"}

app.include_router(v1)


# File Upload

from fastapi import UploadFile, File

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}

# File Download

from fastapi.responses import FileResponse

@app.get("/download")
def download():
    return FileResponse("sample.pdf")

# CORS

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# Custom Exception Handling

from fastapi import HTTPException

@app.get("/{id}")
def student(id: int):

    if id != 1:
        raise HTTPException(404, "Student Not Found")

    return {"id": id}


# Response Models

class StudentOut(BaseModel):
    id: int
    name: str

@app.get("/", response_model=StudentOut)
def home():
    return {
        "id": 1,
        "name": "Alice",
        "password": "123"
    }


# Dependency Injection

from fastapi import Depends

def get_db():
    return "Database"

@app.get("/")
def home(db=Depends(get_db)):
    return {"db": db}

# Background Tasks


from fastapi import BackgroundTasks

def send_email():
    print("Email Sent")

@app.get("/")
def home(task: BackgroundTasks):

    task.add_task(send_email)

    return {"message": "Processing"}

# Middleware

@app.middleware("http")
async def middleware(request, call_next):

    response = await call_next(request)

    return response

# API Testing 

from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200


# Health Check Endpoint

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

