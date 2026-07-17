class Patient:

    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age


class Doctor:

    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization


class Appointment:

    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date


class Hospital:

    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # ---------------- PATIENT ---------------- #

    def add_patient(self):

        patient_id = len(self.patients) + 1

        name = input("Enter Patient Name: ")

        age = int(input("Enter Age: "))

        patient = Patient(patient_id, name, age)

        self.patients.append(patient)

        print("Patient Registered Successfully!")

    # ---------------- DOCTOR ---------------- #

    def add_doctor(self):

        doctor_id = len(self.doctors) + 1

        name = input("Enter Doctor Name: ")

        specialization = input("Enter Specialization: ")

        doctor = Doctor(doctor_id, name, specialization)

        self.doctors.append(doctor)

        print("Doctor Added Successfully!")

    # ---------------- VIEW ---------------- #

    def view_patients(self):

        if not self.patients:
            print("No Patients Registered.")
            return

        print("\nPatients")

        for patient in self.patients:

            print(
                f"ID:{patient.patient_id} | Name:{patient.name} | Age:{patient.age}"
            )

    def view_doctors(self):

        if not self.doctors:
            print("No Doctors Available.")
            return

        print("\nDoctors")

        for doctor in self.doctors:

            print(
                f"ID:{doctor.doctor_id} | Name:{doctor.name} | Specialization:{doctor.specialization}"
            )

    # ---------------- APPOINTMENT ---------------- #

    def book_appointment(self):

        if not self.patients:
            print("Register Patient First.")
            return

        if not self.doctors:
            print("Add Doctor First.")
            return

        self.view_patients()

        patient_id = int(input("Enter Patient ID: "))

        patient = None

        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p
                break

        if patient is None:
            print("Patient Not Found.")
            return

        self.view_doctors()

        doctor_id = int(input("Enter Doctor ID: "))

        doctor = None

        for d in self.doctors:
            if d.doctor_id == doctor_id:
                doctor = d
                break

        if doctor is None:
            print("Doctor Not Found.")
            return

        date = input("Enter Appointment Date: ")

        appointment = Appointment(patient, doctor, date)

        self.appointments.append(appointment)

        print("Appointment Booked Successfully!")

    # ---------------- VIEW APPOINTMENTS ---------------- #

    def view_appointments(self):

        if not self.appointments:
            print("No Appointments.")
            return

        print("\nAppointments")

        for appointment in self.appointments:

            print("-----------------------------------")

            print("Patient :", appointment.patient.name)

            print("Doctor :", appointment.doctor.name)

            print("Specialization :", appointment.doctor.specialization)

            print("Date :", appointment.date)

    # ---------------- MENU ---------------- #

    def menu(self):

        while True:

            print("""
========= Hospital Appointment System =========

1. Register Patient
2. Add Doctor
3. View Patients
4. View Doctors
5. Book Appointment
6. View Appointments
7. Exit

===============================================
""")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_patient()

            elif choice == "2":
                self.add_doctor()

            elif choice == "3":
                self.view_patients()

            elif choice == "4":
                self.view_doctors()

            elif choice == "5":
                self.book_appointment()

            elif choice == "6":
                self.view_appointments()

            elif choice == "7":
                print("Thank You!")
                break

            else:
                print("Invalid Choice")


hospital = Hospital()

hospital.menu()