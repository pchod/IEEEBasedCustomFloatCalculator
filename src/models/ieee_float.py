# ieee_float.py

from models.ieee_format import IEEEFormat

class IEEEfloat:
    """IEEE 754 float representation"""

    def __init__(self, ieee_format: IEEEFormat, sign_bit: str, exponent: str, calculated_exponent: int, mantissa: str, binary_number: str, decimal_number: float, is_precise: bool):
        self.ieee_format = None
        self.sign_bit = None
        self.exponent = None
        self.calculated_exponent = None
        self.mantissa = None
        self.is_precise = None