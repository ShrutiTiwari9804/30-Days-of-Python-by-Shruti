#   HTTP Methods

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"method": "GET"}

@app.post("/")
def create():
    return {"method": "POST"}

@app.put("/")
def update():
    return {"method": "PUT"}

@app.patch("/")
def partial_update():
    return {"method": "PATCH"}

@app.delete("/")
def delete():
    return {"method": "DELETE"}


# Resources (/students)

from fastapi import FastAPI

app = FastAPI()

students = [
    {"id":1,"name":"Alice"},
    {"id":2,"name":"Bob"}
]

@app.get("/students")
def get_students():
    return students

#  URL Parameters (Path Parameters)


from fastapi import FastAPI

app = FastAPI()

@app.get("/students/{student_id}")
def student(student_id: int):
    return {
        "student_id": student_id
    }



# Query Parameters


from fastapi import FastAPI

app = FastAPI()

@app.get("/students")
def students(department: str):
    return {
        "department": department
    }


# Request Body


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def add_student(student: Student):
    return student


# Response


from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {
        "message":"Hello World"
    }


# Status Codes

"""
 Code  Meaning               
 ----  --------------------- 
 200   Success               
 201   Created               
 204   No Content            
 400   Bad Request           
 401   Unauthorized          
 403   Forbidden             
 404   Not Found             
 500   Internal Server Error 

"""

eg ,

from fastapi import FastAPI, status

app = FastAPI()

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create():
    return {"message":"Student Added"}

# Headers

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
def home(user_agent: str = Header()):
    return {
        "Browser": user_agent
    }


# CRUD Operations

from fastapi import FastAPI

app = FastAPI()

students = []

@app.post("/students")
def create(student: dict):
    students.append(student)
    return student

@app.get("/students")
def read():
    return students

@app.put("/students/{id}")
def update(id: int):
    return {"updated": id}

@app.delete("/students/{id}")
def delete(id: int):
    return {"deleted": id}