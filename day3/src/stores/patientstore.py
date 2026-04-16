"""
create patient curd operations
"""
import sys
import os
from models.patient import Patient
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
logger = setup_logger() 
class PatientStore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)

    def get_patient_by_id(self, patient_id: int):
        logger.info(f"Getting patient by id: {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise patient_notfound_exception.PatientNotFoundException(f"Patient with id {patient_id} not found")

    def get_all_patients(self):
        logger.info("Getting all patients")
        return self.patients

    def update_patient(self, patient_id: int, name: str = None, age: int = None):
        logger.info(f"Updating patient: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            logger.info(f"Patient updated: {patient}")
            return patient
        return None

    def delete_patient(self, patient_id: int):
        logger.info(f"Deleting patient: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        
        if patient:
            self.patients.remove(patient)
            logger.info(f"Patient deleted: {patient}")
            return True
        
        logger.warning(f"Patient with id {patient_id} not found")
        return False