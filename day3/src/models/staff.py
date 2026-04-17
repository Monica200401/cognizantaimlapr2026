"""create class staff inherits from person and assosoiated to role as attribute"""
from src.models.person import Person
from src.models.role import Role
class Staff(Person):
    """Staff model definition."""

    def __init__(self, adharcard: str, mobileno: int, role: Role):
        super().__init__(adharcard, mobileno)
        self.__role = role

    @property
    def role(self):
        """Get the role of the staff."""
        return self.__role
    @role.setter
    def role(self, value: Role):
        """Set the role of the staff."""
        self.__role = value