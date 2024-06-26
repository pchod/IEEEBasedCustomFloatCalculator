# number_representation.py

from models.binary_number import BinaryNumber
from models.denary_number import *
from models.ieee_format import IEEEFormat
from models.ieee_float import IEEEfloat

from src.models.denary_number import FractionalNumber, DecimalNumber


class NumberRepresentation:
    """Composite class that represents a number in all its forms"""

    def __init__(
            self,
            ieee_format: IEEEFormat = None,
            binary_number: BinaryNumber = None,
            decimal_number: DecimalNumber = None,
            fractional_number: FractionalNumber = None,
            ieee_float: IEEEfloat = None,
    ) -> None:
        self.ieee_format = ieee_format
        self.binary_number = binary_number
        self.denary = decimal_number if decimal_number is not None else fractional_number
        self.ieee_float = ieee_float

    def is_fractional(self):
        return isinstance(self.denary, FractionalNumber)

    def is_decimal(self):
        return isinstance(self.denary, DecimalNumber)
