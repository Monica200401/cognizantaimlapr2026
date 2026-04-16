""" create doctore curd operations """
import sys
import os
from models.doctor import Doctor
from exceptions import doctornotfoundexception
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
logger = setup_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)

    def get_doctor_by_id(self, doctor_id: int):
        logger.info(f"Getting doctor by id: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise doctor_notfound_exception.DoctorNotFoundException(f"Doctor with id {doctor_id} not found")

    def get_all_doctors(self):
        logger.info("Getting all doctors")
        return self.doctors

    def update_doctor(self, doctor_id: int, name: str = None, specialty: str = None):
        logger.info(f"Updating doctor: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
            logger.info(f"Doctor updated: {doctor}")
            return doctor
        
    def delete_doctor(self, doctor_id: int):
        logger.info(f"Deleting doctor: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        
        if doctor:
            self.doctors.remove(doctor)
            logger.info(f"Doctor deleted: {doctor}")
            return True
        