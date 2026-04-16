# Healthcare Application

This project contains the healthcare application modules for a simple healthcare lookup system.
It includes fake patient and doctor data, plus a display flow that prints patient-to-doctor assignments.

## Setup from scratch

1. Create a new virtual environment:

```bash
python3 -m venv healthenv
```

2. Activate the environment:

```bash
source healthenv/bin/activate
```

3. Install build dependencies and the package in editable mode:

```bash
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -e .
```

## Run the app

```bash
python3 src/app.py
```

## Expected output

The application prints patient-to-doctor assignments in this format:

```text
Patient Name(Disease) -> Doctor Name(Specialization)
```

Example output:

```text
Hannah Barrett(Diabetes) -> Kimberly Dixon(Endocrinologist)
Richard Wall(Skin Rash) -> William Martinez(Dermatologist)
```

## Project structure

- `src/app.py` — application entry point
- `src/models/doctor.py` — doctor model and Faker-backed specialization generation
- `src/models/patient.py` — patient model and Faker-backed disease generation
- `src/store/health_store.py` — builds patient-doctor pairs using disease-to-specialty matching
- `src/view/health_view.py` — formats and prints the output

## Notes

- `pyproject.toml` defines the project metadata and editable install support.
- `README.md` must exist at the project root for the packaging build.
