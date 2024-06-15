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
                 is_positive: bool = None,
                 is_precise: bool = None,
                 rounded_by: str = None,
                 is_special: bool = None):
        self.ieee_format = ieee_format
        self.sign_bit = sign_bit
        self.exponent = exponent
        self.calculated_exponent = calculated_exponent
        self.mantissa = mantissa
        self.is_positive = is_positive
        self.is_precise = is_precise
        self.rounded_by = rounded_by
        self.is_special = is_special
        self.binary_to_convert = binary_to_convert
        # Set sign_bit and is_positive based on each other
        if self.sign_bit is None and self.is_positive is not None:
            self.sign_bit = "0" if self.is_positive else "1"
        if self.is_positive is None and self.sign_bit is not None:
            self.is_positive = self.sign_bit == "0"
