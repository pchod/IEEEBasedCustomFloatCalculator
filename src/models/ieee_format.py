# ieee_format.py


class IEEEFormat:
    """Class representing the custom format for the IEEE binary conversion"""

    SIGN_BIT_LENGTH = 1

    def __init__(self, exponent_length, mantissa_length):
        self.exponent_length = exponent_length
        self.mantissa_length = mantissa_length
        self.bias = 2 ** (len(str(exponent_length)) - 1) - 1
