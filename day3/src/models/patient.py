"""
create patient
"""
from datetime import datetime
import typing
class Patient:
    def __init__(self, id: int, name: str, dob: datetime, ailment: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.ailment = ailment
    def __str__(self):
        return f"Patient(id={self.id}, name='{self.name}', dob='{self.dob}', ailment='{self.ailment}')"