# denary_numbers.py


class DenaryNumber:
    """A parent class for representation of denary numbers"""

    def convert_to_fractional(self):
        raise NotImplementedError

    def convert_to_decimal(self):
        raise NotImplementedError


class FractionalNumber(DenaryNumber):
    """ """

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        # self.bin_denominator = bin(self.denominator)
        # self.bin_denominator_subtracted = bin(self.denominator - 1)

    # def to_binary(self):

    # def is_den_power_of_2(self):


class DecimalNumber(DenaryNumber):
    """ """

    def __init__(self, decimal_number: float):
        self.decimal_number = decimal_number
        self.is_positive = decimal_number > 0
        self.int_part = int(self.decimal_number)
        self.decimal_part = abs(self.decimal_number) - abs(self.int_part)
