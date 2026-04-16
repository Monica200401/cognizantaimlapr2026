from collections import defaultdict

from models.doctor import Doctor
from models.patient import DISEASE_SPECIALTY_MAP, Patient


class HealthStore:
    def __init__(self):
        self.patients = [Patient.fake() for _ in range(4)]
        self.doctors = self._build_doctors_for_patients(self.patients)
        self.patient_doctor_pairs = [
            (patient, self._find_doctor_for_disease(patient.disease))
            for patient in self.patients
        ]

    def _build_doctors_for_patients(self, patients):
        specialties = {DISEASE_SPECIALTY_MAP[patient.disease] for patient in patients}
        doctor_map = defaultdict(list)
        for specialty in specialties:
            doctor_map[specialty].append(Doctor.fake(specialization=specialty))
        return doctor_map

    def _find_doctor_for_disease(self, disease):
        specialty = DISEASE_SPECIALTY_MAP.get(disease, "General Medicine")
        return self.doctors[specialty][0]

    def get_patient_doctor_pairs(self):
        return self.patient_doctor_pairs
