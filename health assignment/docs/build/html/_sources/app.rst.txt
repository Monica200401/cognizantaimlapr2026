Application Overview
====================

Healthcare Management System
-----------------------------

The Healthcare Management System is a Python application that demonstrates the Model-View-Store pattern. It manages:

- **Departments**: 4 specialized departments (Cardiology, Orthopedics, Neurology, Pediatrics)
- **Doctors**: 12 doctors (3 per department) with experience levels
- **Patients**: 50 patients with various diseases
- **Mapping**: Automatic assignment of patients to doctors based on diseases

Architecture
~~~~~~~~~~~~

Models (src/models/)
^^^^^^^^^^^^^^^^^^^^

**Department** (`department.py`)
- Represents a medical department
- Attributes: dept_id, dept_name, specialization

**Doctor** (`doctor.py`)
- Represents a doctor with specialization
- Attributes: doctor_id, name, email, department_id, specialization, experience

**Patient** (`patient.py`)
- Represents a patient with a disease
- Attributes: patient_id, name, email, dob, disease, department_id, assigned_doctor
- Methods: assign_doctor()

Store (src/store/)
^^^^^^^^^^^^^^^^^^

**DepartmentStore** (`departmentstore.py`)
- Manages 4 departments
- Maps diseases to appropriate departments
- Methods: get_departments(), get_department_by_disease()

**DoctorStore** (`doctorstore.py`)
- Generates 12 doctors using Faker
- Methods: get_doctors(), get_doctors_by_department()

**PatientStore** (`patientstore.py`)
- Generates 50 patients with realistic data
- Methods: get_patients(), get_patients_by_disease()

**MappingStore** (`mappingstore.py`)
- Maps patients to doctors based on disease
- Automatically assigns doctors to patients
- Methods: get_mapping(), get_patients_for_doctor()

View (src/view/)
^^^^^^^^^^^^^^^^

**DepartmentView** (`departmentview.py`)
- Displays department information

**DoctorView** (`doctorview.py`)
- Displays doctor information

**PatientView** (`patientview.py`)
- Displays patient information

**MappingView** (`mappingview.py`)
- Displays patient-to-doctor mappings

Running the Application
-----------------------

.. code-block:: bash

    cd src
    python app.py

Output
~~~~~~

The application displays:

1. **Departments** - All 4 departments with specializations
2. **Doctors** - All 12 doctors grouped by department
3. **Patients** - All 50 patients with assigned doctors
4. **Mappings** - Complete patient-to-doctor assignments

Example Output
~~~~~~~~~~~~~~

.. code-block:: text

    ================================================================================
                                 HEALTHCARE DEPARTMENTS
    ================================================================================
    Department(id=DEPT001, name=Cardiology, ...)
    Department(id=DEPT002, name=Orthopedics, ...)
    ...

    ========================================================================================================================
                                                       HEALTHCARE DOCTORS
    ========================================================================================================================
    Doctor(id=DOC001, name=Kathy Barnett, dept_id=DEPT001, ...)
    ...

Disease-Department Mapping
---------------------------

The following diseases are mapped to departments:

- **Cardiology (DEPT001)**: Heart Attack, Chest Pain, Cardiac Arrhythmia
- **Orthopedics (DEPT002)**: Fracture, Arthritis, Back Pain
- **Neurology (DEPT003)**: Headache, Migraine, Seizures
- **Pediatrics (DEPT004)**: Fever, Asthma, Cough

Code Example
~~~~~~~~~~~~

.. code-block:: python

    from store.patientstore import PatientStore
    from store.doctorstore import DoctorStore
    from store.departmentstore import DepartmentStore
    from store.mappingstore import MappingStore

    # Create stores
    patient_store = PatientStore(num_patients=50)
    doctor_store = DoctorStore(num_doctors=12)
    dept_store = DepartmentStore()

    # Map patients to doctors
    mapping_store = MappingStore(patient_store, doctor_store, dept_store)

    # Get results
    mappings = mapping_store.get_mapping()
    for doctor_id, patients in mappings.items():
        print(f"Doctor {doctor_id} has {len(patients)} patients")

Building Documentation
----------------------

To generate HTML documentation:

.. code-block:: bash

    cd docs
    make html

The HTML documentation will be generated in `docs/build/html/`.

View the documentation:

.. code-block:: bash

    open build/html/index.html

Development Workflow
--------------------

Install Development Tools
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install -e ".[dev]"

Format Code
~~~~~~~~~~~

.. code-block:: bash

    black src/ --line-length 88

Sort Imports
~~~~~~~~~~~~

.. code-block:: bash

    isort src/

Lint Code
~~~~~~~~~

.. code-block:: bash

    flake8 src/

Build Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd docs
    make html

Key Concepts
------------

1. **Models**: Classes that represent entities (Doctor, Patient, Department)
2. **Stores**: Classes that manage collections of models and business logic
3. **Views**: Classes that format and display data
4. **Faker**: Library for generating realistic test data
5. **Virtual Environment**: Isolated Python environment for the project
6. **Sphinx**: Documentation generation tool

Learning Outcomes
-----------------

- Understand MVC/MVS (Model-View-Store) architecture
- Work with object-oriented programming in Python
- Use libraries like Faker for data generation
- Build documentation with Sphinx
- Manage Python projects with pyproject.toml
- Use virtual environments for project isolation
