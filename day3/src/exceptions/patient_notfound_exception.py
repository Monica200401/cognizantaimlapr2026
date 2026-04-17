"""
create patient not found exception
"""

class PatientNotFoundException(Exception):
    def __init__(self, message="Patient not found"):
        self.message = message
        super().__init__(message)
