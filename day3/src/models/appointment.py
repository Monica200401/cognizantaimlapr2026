"""
create appointment
"""
from datetime import date, time

class Appointment:
    def __init__(self, id: int, date: date, time: time, doctor=None, patient=None):
        self.id = id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(id={self.id}, doctor={self.doctor}, patient={self.patient}, date='{self.date}', time='{self.time}')"