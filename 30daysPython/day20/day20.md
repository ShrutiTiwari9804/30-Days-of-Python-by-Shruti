# 🎟️ Ticket Booking System (Day 20)

## 📌 Project Overview

A console-based Ticket Booking System built using Python Object-Oriented Programming.

Users can:

- Book tickets
- View bookings
- Update seat count
- Cancel bookings

Booking data is permanently stored using JSON.

---

## Features

- Create Booking
- View All Bookings
- Update Booking
- Delete Booking
- File Storage
- Exception Handling
- Menu Driven Program

---

## OOP Concepts Used

### Classes & Objects
MovieTicket and BookingManager are implemented as classes.

### Encapsulation
Private attributes:

- __booking_id
- __name
- __movie
- __seats

Accessed using getter methods.

### Inheritance
MovieTicket inherits from the abstract Ticket class.

### Abstraction
Ticket is an abstract class using the abc module.

### Polymorphism
The `ticket_details()` method is implemented differently by MovieTicket.

### Composition
BookingManager manages MovieTicket objects and coordinates all booking operations.

---

## CRUD Operations

### Create
Book a new ticket.

### Read
Display all bookings.

### Update
Modify the number of booked seats.

### Delete
Cancel a booking.

---

## File Handling

Bookings are stored in:

```
bookings.json
```

Data persists after the program closes.

---

## Technologies Used

- Python
- OOP
- JSON
- File Handling
- Exception Handling

---

## Sample Menu

```
===== Ticket Booking System =====

1. Book Ticket
2. View Bookings
3. Update Booking
4. Cancel Booking
5. Exit
```

---

## Future Improvements

- Seat availability tracking
- Price calculation
- Movie timings
- User Login
- Admin Panel
- Email Confirmation
- QR Code Ticket Generation

---

## Learning Outcomes

This project helped practice:

- Object-Oriented Programming
- CRUD Operations
- JSON File Handling
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
- Composition
- Exception Handling
- Menu-driven application design