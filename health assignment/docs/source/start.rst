Getting Started
===============

Installation Steps
------------------

Follow these steps to set up and run the Healthcare Management System:

Step 1: Navigate to Project Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd "/workspaces/cognizantaimlapr2026/health assignment"

Step 2: Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    python3 -m venv healthenv

Step 3: Activate Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Linux/Mac:

.. code-block:: bash

    source healthenv/bin/activate

On Windows:

.. code-block:: bash

    healthenv\Scripts\activate

Step 4: Upgrade pip
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install --upgrade pip

Step 5: Install Project with Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install -e .

This installs the healthcare project and required dependencies (faker) from pyproject.toml.

Step 6: Run the Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd src
    python app.py

Complete Quick Setup
--------------------

Run this one-liner to set up everything:

.. code-block:: bash

    cd "/workspaces/cognizantaimlapr2026/health assignment" && python3 -m venv healthenv && source healthenv/bin/activate && pip install --upgrade pip && pip install -e . && cd src && python app.py

Project Structure
-----------------

.. code-block:: text

    health assignment/
    ├── pyproject.toml              # Project configuration
    ├── README.md                   # Project documentation
    ├── docs/                       # Sphinx documentation
    │   ├── source/
    │   │   ├── conf.py            # Sphinx config
    │   │   ├── index.rst          # Documentation homepage
    │   │   ├── start.rst          # Getting started guide
    │   │   └── app.rst            # Application documentation
    │   ├── build/                 # Generated HTML documentation
    │   ├── Makefile               # Build documentation
    │   └── make.bat               # Build documentation (Windows)
    ├── healthenv/                 # Virtual environment folder
    └── src/
        ├── models/                # Data models
        │   ├── department.py
        │   ├── doctor.py
        │   └── patient.py
        ├── store/                 # Business logic
        │   ├── departmentstore.py
        │   ├── doctorstore.py
        │   ├── patientstore.py
        │   └── mappingstore.py
        ├── view/                  # Presentation layer
        │   ├── departmentview.py
        │   ├── doctorview.py
        │   ├── patientview.py
        │   └── mappingview.py
        └── app.py                 # Entry point

What You'll Learn
-----------------

- Object-oriented Python programming
- Model-View-Store architectural pattern
- Working with virtual environments
- Managing dependencies with pip and pyproject.toml
- Sphinx documentation generation
- Faker library for generating realistic test data
