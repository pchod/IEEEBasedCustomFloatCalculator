# number_representation.py

from models.binary_number import BinaryNumber
from models.denary_number import DenaryNumber
from models.ieee_format import IEEEFormat


class NumberRepresentation:
    def __init__(
        self,
        ieee_format: IEEEFormat,
        binary_number: BinaryNumber,
        denary_number: DenaryNumber,
    ) -> None:
        self.ieee_format = ieee_format
        self.binary_number = binary_number
        self.denary_number = denary_number
