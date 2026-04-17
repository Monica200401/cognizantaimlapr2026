import sys
import os


# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from faker import Faker
from src.models.person import Person
from conf.logger_conf import setup_logger
from src.models.role import Role
from src.models.staff import Staffgi
logger = setup_logger("main.log")
def create_person():
    """
    create person object and return it
    """

    person = Person(adharcard="1234-5678-9012", mobileno=9876543210)
    print(f"Person created: Adharcard: {person.adharcard}, Mobileno: {person.mobileno}")
    # update mobileno and print the updated mobileno
    faker = Faker()
    try:
        person.mobileno = int(faker.numerify(text='##########'))
        logger.info(f"Updated mobileno: {person.mobileno}")
    except Exception as e:
        logger.error(f"Error updating mobileno: {e}")

def create_staff():
    """
    create staff object and return it
    """
    from src.models.staff import Staff
    from src.models.role import Role
    role = Role(id=1, name="Nurse")
    staff = Staff(adharcard="9876-5432-1098", mobileno=1234567890, role=role)
    print(f"Staff created: Adharcard: {staff.adharcard}, Mobileno: {staff.mobileno}, Role: {staff.role.name}")
    return staff

if __name__ == "__main__":
    create_person()
    create_staff()