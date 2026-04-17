"""
test for doctor contract
"""
 
import sys
import os
import csv
import pytest
 
# add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
 
from src.models.doctor import Doctor
 
"""
test for doctor object created
"""
@pytest.fixture
def initialize_doctor():
    doctor = Doctor(id=1, name="Aditya Verma", specialization="Cardiology")
    return doctor
 
 
def read_doctor_data_from_csv():
    """
    read doctor data from csv file and return as list of tuples
    """

    doctors_data = []
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'doctors.csv')
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            specialty = row.get('specialty') or row.get('specialization')
            doctors_data.append((int(row['id']), row['name'], specialty))
    return doctors_data
 
 
def test_doctor_creation(initialize_doctor):
    doctor = initialize_doctor
    assert doctor.id == 1
    assert doctor.name == "Aditya Verma"
    assert doctor.specialization == "Cardiology"
 
@pytest.mark.parametrize("id, name, specialization", [
    (2, "Balu Subramanian", "Neurology"),    
    (3, "Challa Nithya", "Dermatology"),
    (4, "Deshpande Harsha", "Endocrinology"),
    (5, "Emaddi Keerthana", "General Practice"),
])
def test_parameterized_doctor_creation(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization
 
@pytest.mark.parametrize("id, name, specialization", read_doctor_data_from_csv())
def test_parameterized_csv(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization
 