import json
import os
from abc import ABC, abstractmethod

FILE_NAME = "bookings.json"

# File Handling

def load_data():
    if os.path.exists(FILE_NAME):
        with open (FILE_NAME,'r') as file:
            return json.load(file)
        return[]
    

def save_data(data):
    with open(FILE_NAME,'w') as file:
        json.dump(data, file, indent=4)


# Abstraction

class Ticket(ABC):

    @abstractmethod
    def ticket_details(self):
        pass


# Inheritance

class MovieTicket(Ticket):

    def __init__ (self, booking_id, name, movie, seats):
        self.__booking_id = booking_id      # Encapsulation
        self.__name = name
        self.__movie = movie
        self.__seats = seats


    # Getter Methods

    def get_booking_id (self):
        return self.__booking_id
    
    def get_name(self):
        return self.__name
    
    def get_movie(self):
        return self.__movie
    
    def get_seats(self):
        return self.__seats
    

    # Setter 

    def ticket_details(self):
        return {
            "Booking ID " : self.__booking_id,
            "Customer" : self.__name,
            "Movie": self.__movie,
            "Seats": self.__seats
        }
    

# Composition

class BookingManager:

    def __init__(self):
        self.bookings = load_data()

    def create_booking(self):

        booking_id = input("Booking ID: ")

        for bookings in self.bookings:
            if booking ["Booking ID"] == booking_id:
                print("Booking ID already Exists.")
                return
            
        name = input("Customer Name: ")
        movie = input ("Movie Name: ")

        try:
            seats = int(input("Number Of Seats: "))
        except ValueError:
            print("Invalid number.")
            return
        
        ticket = MovieTicket(booking_id, name, movie, seats)

        self.bookings.append(ticket.ticket_details())
        save_data(self.bookings)

        print("Booking Successful!")


    def view_bookings(self):

        if not self.bookings:
            print("No Bookings Found")
            return
        
        for booking in self.bookings:
            print("-" * 40)
            for key , value in booking.items():
                print(f"{key}: {value}")

    
    def update_booking(self):

        booking_id = input("Enter Booking ID: ")

        for booking in self.bookings:

            if booking ["Booking ID"] == booking_id:

                try: 
                    seats = int(input("New Seat Count: "))
                except ValueError:
                    print("Invalid input")
                    return
                
                booking ["Seats"] = seats
                save_data(self.bookings)

                print("Booking Updated")
                return
            
        print("Booking Not Found")

    def delete_booking(self):

        booking_id = input("Enter Booking ID: ")

        for booking in self.bookings:

            if booking [" Booking ID"] == booking_id:
                self.bookings.remove(booking)
                save_data(self.bookings)
                print("Booking Cancelled")
                return
            
        print("Booking Not Found.")

