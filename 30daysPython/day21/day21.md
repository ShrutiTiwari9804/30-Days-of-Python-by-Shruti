# 🚖 Day 21 - Cab Booking System

## 📌 Project Description

This is a simple Cab Booking System developed using Python and Object-Oriented Programming (OOP). The project allows users to create, view, search, update, and cancel cab bookings. Booking information is stored permanently in a JSON file using file handling.

---

## ✨ Features

- Book a Cab
- View All Bookings
- Search Booking by ID
- Update Booking
- Cancel Booking
- Store data using JSON
- CRUD Operations
- Exception Handling

---

## 🛠 Technologies Used

- Python
- Object-Oriented Programming
- JSON File Handling

---

## 📂 Files Used

```
day21.py
bookings.json
day21.md
```

---

# OOP Concepts Used

## 1. Class

Three classes are created.

- Booking
- CabBooking
- BookingManager

Example:

```python
class CabBooking(Booking):
```

---

## 2. Object

An object of the CabBooking class is created.

```python
booking = CabBooking(
    booking_id,
    customer,
    pickup,
    destination,
    cab_type
)
```

---

## 3. Constructor

The constructor initializes object data.

```python
def __init__(self, booking_id, customer, pickup, destination, cab_type):
```

---

## 4. Encapsulation

Private variables are used.

```python
self.__booking_id
self.__customer
self.__pickup
self.__destination
self.__cab_type
```

Getter methods are provided to access them.

---

## 5. Abstraction

The Booking class is an abstract class.

```python
from abc import ABC, abstractmethod

class Booking(ABC):

    @abstractmethod
    def booking_details(self):
        pass
```

---

## 6. Inheritance

CabBooking inherits Booking.

```python
class CabBooking(Booking):
```

---

## 7. Polymorphism

The abstract method is overridden.

```python
def booking_details(self):
```

---

## 8. File Handling

JSON is used to permanently store bookings.

```python
json.load()

json.dump()
```

---

## 9. CRUD Operations

### Create

Book a new cab.

### Read

Display all bookings.

### Update

Modify booking details.

### Delete

Cancel booking.

---

## 10. Exception Handling

Invalid user input is handled using try-except blocks.

Example:

```python
try:
    seats = int(input())
except ValueError:
    print("Invalid Input")
```

---

# Sample Output

```
========== CAB BOOKING SYSTEM ==========

1. Book Cab
2. View Bookings
3. Search Booking
4. Update Booking
5. Cancel Booking
6. Exit

Enter Choice: 1

Booking ID: 101
Customer Name: Shruti
Pickup Location: Pune
Destination: Mumbai
Cab Type: Sedan

Cab Booked Successfully!
```

---

# Learning Outcomes

After completing this project I learned:

- Object-Oriented Programming
- Constructors
- Classes and Objects
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
- CRUD Operations
- JSON File Handling
- Exception Handling
- Python Project Structure

---

## Author

**Shruti Tiwari**

30 Days of Python Challenge 🚀