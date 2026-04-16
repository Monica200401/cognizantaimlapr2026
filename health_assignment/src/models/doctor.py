from faker import Faker

fake = Faker()

SPECIALIZATIONS = [
    "General Medicine",
    "Cardiology",
    "Neurology",
    "Endocrinology",
    "Pediatrics",
    "Dermatology",
    "Orthopedics",
    "Psychiatry",
]


class Doctor:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization

    @classmethod
    def fake(cls, specialization: str | None = None):
        return cls(
            name=fake.name(),
            specialization=specialization or fake.random_element(SPECIALIZATIONS),
        )

    def __str__(self) -> str:
        return f"{self.name}({self.specialization})"

    def __repr__(self) -> str:
        return str(self)
