"""
test for patient contract
"""

import sys
import os
import csv
from datetime import datetime
import pytest

# add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.models.patient import Patient

"""
test for patient object created
"""
@pytest.fixture
def initialize_patient():
    patient = Patient(id=1, name="Ananya Sharma", dob=datetime.strptime("1990-05-18", "%Y-%m-%d"), ailment="Diabetes")
    return patient


def read_patient_data_from_csv():
    """
    read patient data from csv file and return as list of tuples
    """

    patients_data = []
    csv_path = os.path.join(os.path.dirname(__file__), 'patient.csv')
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients_data.append((
                int(row['id']),
                row['name'],
                datetime.strptime(row['dob'], '%Y-%m-%d'),
                row['ailment']
            ))
    return patients_data


def test_patient_creation(initialize_patient):
    patient = initialize_patient
    assert patient.id == 1
    assert patient.name == "Ananya Sharma"
    assert patient.dob == datetime.strptime("1990-05-18", "%Y-%m-%d")
    assert patient.ailment == "Diabetes"

@pytest.mark.parametrize("id, name, dob, ailment", [
    (2, "Rohan Mehta", datetime.strptime("1985-11-02", "%Y-%m-%d"), "Hypertension"),
    (3, "Neha Patel", datetime.strptime("2001-07-22", "%Y-%m-%d"), "Asthma"),
    (4, "Karan Singh", datetime.strptime("1979-12-15", "%Y-%m-%d"), "Back pain"),
    (5, "Meera Iyer", datetime.strptime("1994-02-08", "%Y-%m-%d"), "Migraine"),
])
def test_parameterized_patient_creation(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment

@pytest.mark.parametrize("id, name, dob, ailment", read_patient_data_from_csv())
def test_parameterized_csv(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment
