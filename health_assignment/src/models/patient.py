from faker import Faker

fake = Faker()

DISEASES = [
    "Flu",
    "Migraine",
    "Diabetes",
    "Hypertension",
    "Asthma",
    "Allergies",
    "Back Pain",
    "Skin Rash",
]


DISEASE_SPECIALTY_MAP = {
    "Flu": "General Medicine",
    "Migraine": "Neurology",
    "Diabetes": "Endocrinology",
    "Hypertension": "Cardiology",
    "Asthma": "General Medicine",
    "Allergies": "Dermatology",
    "Back Pain": "Orthopedics",
    "Skin Rash": "Dermatology",
}


class Patient:
    def __init__(self, name: str, disease: str):
        self.name = name
        self.disease = disease

    @classmethod
    def fake(cls, disease: str | None = None):
        disease = disease or fake.random_element(DISEASES)
        return cls(
            name=fake.name(),
            disease=disease,
        )

    def __str__(self) -> str:
        return f"{self.name}({self.disease})"

    def __repr__(self) -> str:
        return str(self)
