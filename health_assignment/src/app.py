from store.health_store import HealthStore
from view.health_view import print_patient_doctor_pairs


def main() -> None:
    store = HealthStore()
    pairs = store.get_patient_doctor_pairs()
    print_patient_doctor_pairs(pairs)


if __name__ == "__main__":
    main()
