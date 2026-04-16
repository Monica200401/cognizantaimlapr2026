from models.doctor import Doctor
from models.patient import Patient


def format_patient_doctor_pair(patient: Patient, doctor: Doctor) -> str:
    return f"{patient} -> {doctor}"


def print_patient_doctor_pairs(pairs):
    for patient, doctor in pairs:
        print(format_patient_doctor_pair(patient, doctor))
