

# 📖 Concepts Explained

## 1️⃣ POST Request

A POST request is used to **create new resources**.

Examples:

* Register User
* Login
* Add Student
* Add Product
* Place Order

Example:

```python
@app.post("/students")
```

---

## 2️⃣ Request Body

The request body contains the data sent by the client in JSON format.

Example:

```json
{
  "id": 1,
  "name": "Shruti",
  "age": 21,
  "course": "Python"
}
```

FastAPI automatically converts this JSON into a Python object.

---

## 3️⃣ Pydantic Models

Pydantic is used to define the structure of incoming data.

Benefits:

* Automatic Validation
* Type Conversion
* Cleaner Code
* Better Error Messages

Example:

```python
class Student(BaseModel):
    id: int
    name: str
    age: int
```

---

## 4️⃣ Field Validation

The `Field()` function is used to validate individual model fields.

Supported validations include:

* `gt`
* `ge`
* `lt`
* `le`
* `min_length`
* `max_length`

Example:

```python
age: int = Field(..., ge=18, le=60)
```

If invalid data is sent, FastAPI automatically returns:

```text
422 Unprocessable Entity
```

---

## 5️⃣ Optional Fields

Optional fields are not required in every request.

Example:

```python
description: Optional[str] = None
```

Clients can either include the field or omit it.

---

## 6️⃣ Response Models

A Response Model controls what data is returned to the client.

This is useful for hiding sensitive information such as:

* Passwords
* OTPs
* Secret Tokens

Example:

```python
@app.post("/register", response_model=UserResponse)
```

Only the fields defined in `UserResponse` are returned.

---

## 7️⃣ HTTP Status Codes

Common HTTP Status Codes:

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 422  | Validation Error      |
| 500  | Internal Server Error |

---

## 8️⃣ HTTPException

`HTTPException` is used to return custom error messages.

Example:

```python
raise HTTPException(
    status_code=400,
    detail="Invalid Input"
)
```

Instead of crashing, the API returns a proper error response.

---

## 9️⃣ Nested Models

Pydantic models can contain other models.

Example:

```python
Customer
│
└── Address
```

Nested models make it easy to represent complex JSON data structures.

---

# 🧪 API Endpoints

| Endpoint         | Method | Description       |
| ---------------- | ------ | ----------------- |
| `/students`      | POST   | Add Student       |
| `/students/all`  | GET    | View All Students |
| `/employee`      | POST   | Create Employee   |
| `/books`         | POST   | Add Book          |
| `/register`      | POST   | Register User     |
| `/course`        | POST   | Create Course     |
| `/marks/{marks}` | GET    | Validate Marks    |
| `/age/{age}`     | GET    | Age Validation    |
| `/customer`      | POST   | Create Customer   |

---

# 💡 Key Learnings

* Built APIs using POST requests.
* Accepted JSON request bodies.
* Used BaseModel to validate incoming data.
* Applied Field validation rules.
* Created optional fields.
* Returned secure responses using Response Models.
* Implemented HTTP status codes.
* Handled API errors with HTTPException.
* Created nested request models.

