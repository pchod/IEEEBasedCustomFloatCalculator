# ieee_float.py

from ieee_format import IEEEFormat


class IEEEFloat:
    """IEEE 754 float representation"""

    def __init__(self,
                 ieee_format: IEEEFormat = None,
                 sign_bit: str = None,
                 exponent: str = None,
                 calculated_exponent: int = None,
                 mantissa: str = None,
                 binary_to_convert: str = None,
                 is_precise: bool = None,
                 rounded_by: str = None,
                 is_special: bool = None):
        self.ieee_format = ieee_format
        self.sign_bit = sign_bit
        self.exponent = exponent
        self.calculated_exponent = calculated_exponent
        self.mantissa = mantissa
        self.is_precise = is_precise
        self.rounded_by = rounded_by
        self.is_special = is_special
        self.binary_to_convert = binary_to_convert
