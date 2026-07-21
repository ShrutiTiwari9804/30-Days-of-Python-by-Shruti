import json
import os
from abc import ABC, abstractmethod

FILE_NAME = "bookings.json"


# ================= FILE HANDLING =================

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ================= ABSTRACTION =================

class Booking(ABC):

    @abstractmethod
    def booking_details(self):
        pass


# ================= INHERITANCE =================

class CabBooking(Booking):

    # Constructor
    def __init__(self, booking_id, customer, pickup, destination, cab_type):

        # Encapsulation (Private Variables)
        self.__booking_id = booking_id
        self.__customer = customer
        self.__pickup = pickup
        self.__destination = destination
        self.__cab_type = cab_type

    # Getter Methods
    def get_booking_id(self):
        return self.__booking_id

    def get_customer(self):
        return self.__customer

    def get_pickup(self):
        return self.__pickup

    def get_destination(self):
        return self.__destination

    def get_cab_type(self):
        return self.__cab_type

    # Polymorphism (Method Overriding)
    def booking_details(self):

        return {

            "Booking ID": self.__booking_id,
            "Customer": self.__customer,
            "Pickup": self.__pickup,
            "Destination": self.__destination,
            "Cab Type": self.__cab_type

        }


# ================= MANAGER CLASS =================

class BookingManager:

    def __init__(self):
        self.bookings = load_data()

    # ============ CREATE ============

    def create_booking(self):

        booking_id = input("Booking ID : ")

        for booking in self.bookings:
            if booking["Booking ID"] == booking_id:
                print("Booking ID already exists.")
                return

        customer = input("Customer Name : ")

        pickup = input("Pickup Location : ")

        destination = input("Destination : ")

        cab_type = input("Cab Type (Mini/Sedan/SUV): ")

        booking = CabBooking(

            booking_id,
            customer,
            pickup,
            destination,
            cab_type

        )

        self.bookings.append(
            booking.booking_details()
        )

        save_data(self.bookings)

        print("\nCab Booked Successfully!")

    # ============ READ ============

    def view_bookings(self):

        if not self.bookings:
            print("\nNo Bookings Found.")
            return

        print("\n========= BOOKINGS =========\n")

        for booking in self.bookings:

            print(f"Booking ID : {booking['Booking ID']}")
            print(f"Customer   : {booking['Customer']}")
            print(f"Pickup     : {booking['Pickup']}")
            print(f"Destination: {booking['Destination']}")
            print(f"Cab Type   : {booking['Cab Type']}")
            print("-" * 35)