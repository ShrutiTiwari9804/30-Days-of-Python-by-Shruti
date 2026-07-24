# ===================================================================
# PART 2 - POST REQUESTS, PYDANTIC & VALIDATION
# ===================================================================

"""
Topics Covered

1. POST Request
2. Request Body
3. Pydantic Models
4. Response Model
5. Status Codes
6. HTTPException
7. Field Validation
8. Optional Fields
9. Nested Models
"""

from fastapi import HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

# ===================================================================
# WHAT IS A POST REQUEST?
# ===================================================================

"""
GET
↓

Used to READ data.

POST
↓

Used to CREATE data.

Real World Examples

POST /register

POST /login

POST /create-user

POST /add-product

POST /place-order
"""

# Fake Database
students = []

# ===================================================================
# PYDANTIC MODEL
# ===================================================================

"""
A Pydantic Model describes the structure of incoming data.

FastAPI automatically:

✔ Validates data
✔ Converts data types
✔ Returns errors if data is invalid
"""

class Student(BaseModel):

    id: int
    name: str
    age: int
    course: str


"""
Expected JSON

{
    "id":1,
    "name":"Shruti",
    "age":21,
    "course":"Python"
}
"""

# ===================================================================
# FIRST POST REQUEST
# ===================================================================

@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {

        "message": "Student Added Successfully",
        "student": student

    }

"""
Open Swagger

/docs

Choose POST

Click Try it Out

Paste

{
    "id":1,
    "name":"Shruti",
    "age":21,
    "course":"Python"
}

Execute

Output

{
   "message":"Student Added Successfully",
   "student":{

      "id":1,
      "name":"Shruti",
      "age":21,
      "course":"Python"

   }
}
"""

# ===================================================================
# VIEW ALL STUDENTS
# ===================================================================

@app.get("/students/all")
def get_students():

    return students

"""
Output

[
   {
      "id":1,
      "name":"Shruti",
      "age":21,
      "course":"Python"
   }
]
"""

# ===================================================================
# FIELD VALIDATION
# ===================================================================

"""
Field()

Used for validation.

gt -> Greater Than

ge -> Greater Than Equal

lt -> Less Than

le -> Less Than Equal

min_length

max_length
"""

class Employee(BaseModel):

    id: int = Field(..., gt=0)

    name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )

    age: int = Field(
        ...,
        ge=18,
        le=60
    )

    salary: float = Field(
        ...,
        gt=0
    )

"""
Invalid Example

{
   "id":0,
   "name":"A",
   "age":15,
   "salary":-200
}

↓

422 Validation Error
"""

# ===================================================================
# EMPLOYEE API
# ===================================================================

@app.post("/employee")
def create_employee(employee: Employee):

    return {

        "message": "Employee Created",

        "employee": employee

    }

# ===================================================================
# OPTIONAL FIELDS
# ===================================================================

"""
Optional Fields

Not every field is compulsory.

Optional

↓

May contain None.
"""

class Book(BaseModel):

    title: str

    author: str

    pages: int

    price: float

    description: Optional[str] = None

"""
Valid

{
   "title":"Python",
   "author":"ABC",
   "pages":500,
   "price":599
}

Also Valid

{
   "title":"Python",
   "author":"ABC",
   "pages":500,
   "price":599,
   "description":"Best Python Book"
}
"""

@app.post("/books")
def create_book(book: Book):

    return book

# ===================================================================
# RESPONSE MODEL
# ===================================================================

"""
Sometimes

Database contains

password

email

phone

But we don't want to send
everything back.

Response Model decides

What client receives.
"""

class UserRequest(BaseModel):

    username: str

    password: str

    email: str


class UserResponse(BaseModel):

    username: str

    email: str


@app.post("/register", response_model=UserResponse)
def register(user: UserRequest):

    return user

"""
Input

{

 "username":"Shruti",

 "password":"12345",

 "email":"abc@gmail.com"

}

Output

{

 "username":"Shruti",

 "email":"abc@gmail.com"

}

Notice

Password is hidden.
"""

# ===================================================================
# STATUS CODES
# ===================================================================

"""
Common Status Codes

200 OK

201 Created

204 No Content

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

422 Validation Error

500 Internal Server Error
"""

@app.post(
    "/course",
    status_code=status.HTTP_201_CREATED
)
def create_course():

    return {

        "message": "Course Created"

    }

"""
Response Code

201
"""

# ===================================================================
# HTTP EXCEPTION
# ===================================================================

"""
Instead of crashing

Raise HTTPException.
"""

@app.get("/marks/{marks}")
def check_marks(marks: int):

    if marks > 100:

        raise HTTPException(

            status_code=400,

            detail="Marks cannot exceed 100"

        )

    return {

        "Marks": marks

    }

"""
Valid

/marks/90

Output

{

 "Marks":90

}

Invalid

/marks/150

Output

{

 "detail":"Marks cannot exceed 100"

}
"""

# ===================================================================
# MULTIPLE EXCEPTIONS
# ===================================================================

@app.get("/age/{age}")
def check_age(age: int):

    if age < 0:

        raise HTTPException(

            status_code=400,

            detail="Age cannot be negative"

        )

    if age < 18:

        raise HTTPException(

            status_code=403,

            detail="Access Denied"

        )

    return {

        "message": "Access Granted"

    }

# ===================================================================
# NESTED PYDANTIC MODEL
# ===================================================================

"""
Models can contain other models.
"""

class Address(BaseModel):

    city: str

    state: str

    pincode: int


class Customer(BaseModel):

    name: str

    age: int

    address: Address


@app.post("/customer")
def create_customer(customer: Customer):

    return customer

"""
Example JSON

{

 "name":"Shruti",

 "age":21,

 "address":{

    "city":"Pune",

    "state":"Maharashtra",

    "pincode":411001

 }

}
"""

