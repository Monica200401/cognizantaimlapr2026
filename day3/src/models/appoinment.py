"""
create appointment
"""
from datetime import date,time
class Appointment:
    def __init__(self, id: int, patient_id: int, doctor_id: int, date: date, time: time):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
    def __str__(self):
        return f"Appointment(id={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, date='{self.date}', time='{self.time}')"