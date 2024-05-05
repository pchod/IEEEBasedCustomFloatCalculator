# ieee_float.py

from models.ieee_format import IEEEFormat


class IEEEFloat:
    """IEEE 754 float representation"""

    def __init__(self,
                 ieee_format: IEEEFormat,
                 sign_bit: str,
                 exponent: str,
                 calculated_exponent: int,
                 mantissa: str,
                 binary_to_convert: str,
                 is_precise: bool):
        self.ieee_format = ieee_format
        self.sign_bit = sign_bit
        self.exponent = exponent
        self.calculated_exponent = calculated_exponent
        self.mantissa = mantissa
        self.is_precise = is_precise
        self.is_special = None
        self.binary_to_convert = binary_to_convert
