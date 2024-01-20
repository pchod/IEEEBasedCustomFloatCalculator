# number_representation.py

from models.binary_number import BinaryNumber
from models.denary_number import DenaryNumber
from models.ieee_format import IEEEFormat
from models.ieee_float import IEEEfloat


class NumberRepresentation:
    """Composite class that represents a number in all its forms"""
    def __init__(
        self,
        ieee_format: IEEEFormat,
        binary_number: BinaryNumber,
        denary_number: DenaryNumber,
        ieee_float: IEEEfloat,
    ) -> None:
        self.ieee_format = ieee_format
        self.binary_number = binary_number
        self.denary_number = denary_number
        self.ieee_float = ieee_float