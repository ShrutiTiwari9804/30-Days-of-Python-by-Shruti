import json
import os
from abc import ABC, abstractmethod

FILE_NAME = "bookings.json"

# ==========================================================
# FILE HANDLING
# ==========================================================

def load_data():
    """Load booking data from JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    """Save booking data into JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ==========================================================
# ABSTRACTION
# Abstract class representing a Person
# ==========================================================

class Person(ABC):

    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    @abstractmethod
    def display(self):
        pass


# ==========================================================
# INHERITANCE
# Rider inherits Person
# ==========================================================

class Rider(Person):

    def __init__(self, rider_id, name):
        super().__init__(rider_id, name)

    def display(self):
        return {
            "Rider ID": self._person_id,
            "Rider Name": self._name
        }


# ==========================================================
# INHERITANCE
# Driver inherits Person
# ==========================================================

class Driver(Person):

    def __init__(self, driver_id, name, cab_number):
        super().__init__(driver_id, name)
        self._cab_number = cab_number

    def display(self):
        return {
            "Driver ID": self._person_id,
            "Driver Name": self._name,
            "Cab Number": self._cab_number
        }


# ==========================================================
# ENCAPSULATION
# Private fare attribute
# ==========================================================

class Cab:

    def __init__(self, cab_number, cab_type):
        self.__cab_number = cab_number
        self.__cab_type = cab_type

    def get_cab_number(self):
        return self.__cab_number

    def get_cab_type(self):
        return self.__cab_type


# ==========================================================
# ABSTRACTION
# Booking Interface
# ==========================================================

class Booking(ABC):

    @abstractmethod
    def booking_details(self):
        pass


# ==========================================================
# POLYMORPHISM
# CabBooking overrides booking_details()
# ==========================================================

class CabBooking(Booking):

    def __init__(
            self,
            booking_id,
            rider,
            driver,
            cab,
            pickup,
            destination,
            distance):

        # COMPOSITION
        # Booking HAS Rider, Driver and Cab objects

        self.__booking_id = booking_id
        self.__rider = rider
        self.__driver = driver
        self.__cab = cab

        self.__pickup = pickup
        self.__destination = destination
        self.__distance = distance

        self.__fare = self.calculate_fare()

    # ======================================================
    # ENCAPSULATION
    # ======================================================

    def calculate_fare(self):

        if self.__cab.get_cab_type() == "Mini":
            rate = 12

        elif self.__cab.get_cab_type() == "Sedan":
            rate = 18

        else:
            rate = 25

        return rate * self.__distance

    # ======================================================
    # POLYMORPHISM
    # ======================================================

    def booking_details(self):

        return {

            "Booking ID": self.__booking_id,

            "Rider": self.__rider.display(),

            "Driver": self.__driver.display(),

            "Cab": {

                "Cab Number": self.__cab.get_cab_number(),

                "Cab Type": self.__cab.get_cab_type()

            },

            "Pickup": self.__pickup,

            "Destination": self.__destination,

            "Distance": self.__distance,

            "Fare": self.__fare
        }


# ==========================================================
# COMPOSITION
# Bank-like manager class for Cab Bookings
# ==========================================================

class CabBookingManager:

    def __init__(self):

        self.bookings = load_data()

    # ======================================================
    # CRUD - CREATE
    # ======================================================

    def create_booking(self):

        booking_id = input("Booking ID : ")

        for booking in self.bookings:

            if booking["Booking ID"] == booking_id:
                print("Booking ID already exists.")
                return

        rider_name = input("Rider Name : ")

        rider = Rider(
            "R101",
            rider_name
        )

        driver_name = input("Driver Name : ")

        cab_number = input("Cab Number : ")

        cab_type = input(
            "Cab Type (Mini/Sedan/SUV): "
        )

        driver = Driver(
            "D101",
            driver_name,
            cab_number
        )

        cab = Cab(
            cab_number,
            cab_type
        )

        pickup = input("Pickup Location : ")

        destination = input("Destination : ")

        try:

            distance = float(
                input("Distance (KM): ")
            )

        except ValueError:

            print("Invalid distance.")

            return

        booking = CabBooking(

            booking_id,

            rider,

            driver,

            cab,

            pickup,

            destination,

            distance

        )

        self.bookings.append(
            booking.booking_details()
        )

        save_data(self.bookings)

        print("\nBooking Created Successfully!")