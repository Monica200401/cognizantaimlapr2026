"""
application entry point for day 2 project.

"""

import random


def generate_otp():
    """
    this function generates a random 6 digit otp and returns it.

    """

    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
