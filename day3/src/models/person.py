
"""Person model"""
import re
class Person:
    """Person model"""

    def __init__(self, adharcard: str, mobileno: int):
        self.__adharcard = adharcard
        self.__mobileno = mobileno

    @property
    def adharcard(self):
        """Get the adharcard number"""
        return self.__adharcard

    @property
    def mobileno(self):
        """Get the mobile number"""
        return self.__mobileno
    
    #setter for mo
    @mobileno.setter
    def mobileno(self, mobileno):
        if not re.match(r'^\d{10}$', str(mobileno)):
            raise ValueError("Invalid mobile number. It should be a 10-digit number.")
        """Set the mobile number"""
        self.__mobileno = mobileno