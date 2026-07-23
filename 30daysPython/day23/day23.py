"""
===========================================================
                FASTAPI DAY 1 - BASICS
===========================================================

Topics Covered

1. What is FastAPI?
2. Installing FastAPI
3. Creating your First API
4. Running the Server
5. Path Operations
6. Path Parameters
7. Query Parameters

===========================================================
"""

# ---------------------------------------------------------
# WHAT IS FASTAPI?
# ---------------------------------------------------------

"""
FastAPI is a modern Python web framework used for building APIs.

Imagine you are making an online shopping website.

Frontend (HTML, CSS, React)
        |
        | Request
        V
FastAPI (Backend)
        |
        | Talks to Database
        V
Database

FastAPI receives requests from users,
processes them,
and returns responses.

Example:

Browser
↓
GET /products

FastAPI
↓
Returns all products in JSON

Response:

{
    "products":[...]
}

FastAPI is extremely fast because it is built on:

1. Starlette (Web framework)
2. Pydantic (Validation)

Advantages

✔ Very Fast
✔ Easy to Learn
✔ Automatic Documentation
✔ Built-in Validation
✔ Async Support
✔ Used in Production
"""

# ---------------------------------------------------------
# IMPORTING FASTAPI
# ---------------------------------------------------------

"""
Before creating an API, we import FastAPI.
"""

from fastapi import FastAPI

# ---------------------------------------------------------
# CREATING THE APPLICATION
# ---------------------------------------------------------

"""
This line creates the FastAPI application.

Think of it as creating the backend server.

Without this object, nothing works.
"""

app = FastAPI()

# ---------------------------------------------------------
# YOUR FIRST API
# ---------------------------------------------------------

"""
@app.get("/")

This is called a PATH OPERATION DECORATOR.

It means:

Whenever someone visits

http://127.0.0.1:8000/

run the function below.
"""

@app.get("/")
def home():
    """
    Home Route

    Returns a welcome message.
    """

    return {
        "message": "Welcome to FastAPI!"
    }

"""
Output

{
   "message":"Welcome to FastAPI!"
}
"""

# ---------------------------------------------------------
# SECOND ROUTE
# ---------------------------------------------------------

"""
We can create as many routes as we want.
"""

@app.get("/about")
def about():
    return {
        "developer": "Shruti",
        "course": "FastAPI Basics"
    }

"""
Visit

http://127.0.0.1:8000/about

Output

{
   "developer":"Shruti",
   "course":"FastAPI Basics"
}
"""

# ---------------------------------------------------------
# PATH PARAMETERS
# ---------------------------------------------------------

"""
Suppose we want different users.

Example

/user/1

/user/2

/user/100

Instead of creating separate routes,
we use PATH PARAMETERS.
"""

@app.get("/user/{user_id}")
def get_user(user_id: int):
    """
    user_id is received from URL.

    Example

    /user/10

    user_id = 10
    """

    return {
        "User ID": user_id
    }

"""
Examples

/user/1

Output

{
   "User ID":1
}

/user/55

Output

{
   "User ID":55
}
"""

# ---------------------------------------------------------
# MULTIPLE PATH PARAMETERS
# ---------------------------------------------------------

@app.get("/student/{name}/{age}")
def student(name: str, age: int):

    return {
        "Name": name,
        "Age": age
    }

"""
Example

/student/Shruti/21

Output

{
   "Name":"Shruti",
   "Age":21
}
"""

# ---------------------------------------------------------
# QUERY PARAMETERS
# ---------------------------------------------------------

"""
Query parameters come after ?

Example

/search?item=laptop

Here

item=laptop

is a Query Parameter.
"""

@app.get("/search")
def search(item: str):

    return {
        "Searching": item
    }

"""
Example

/search?item=phone

Output

{
   "Searching":"phone"
}
"""

# ---------------------------------------------------------
# MULTIPLE QUERY PARAMETERS
# ---------------------------------------------------------

@app.get("/product")
def product(name: str, price: int):

    return {
        "Product": name,
        "Price": price
    }

"""
Example

/product?name=Laptop&price=50000

Output

{
   "Product":"Laptop",
   "Price":50000
}
"""

# ---------------------------------------------------------
# OPTIONAL QUERY PARAMETERS
# ---------------------------------------------------------

"""
Giving a default value makes a query parameter optional.
"""

@app.get("/books")
def books(category: str = "Programming"):

    return {
        "Category": category
    }

"""
Example

/books

Output

{
   "Category":"Programming"
}

Example

/books?category=Python

Output

{
   "Category":"Python"
}
"""

# ---------------------------------------------------------
# ROOT SUMMARY
# ---------------------------------------------------------

"""
Today I learned:

✔ FastAPI
✔ FastAPI()
✔ Routes
✔ GET Request
✔ Path Parameters
✔ Query Parameters
✔ Optional Query Parameters
"""