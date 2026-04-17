"""Role model definition."""
class Role:
    """
    a class representing a role with a name and description.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    #getter for name
    @property
    def name(self):
        """Get the name of the role."""
        return self.__name
    @property
    def description(self):
        """Get the description of the role."""
        return self.__description
    #setter for description
    @description.setter
    def description(self, description):
        """Set the description of the role."""
        self.__description = description
