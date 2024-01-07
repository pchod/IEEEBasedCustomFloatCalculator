# denary_number.py


from models.ieee_format import IEEEFormat


class DenaryNumber:
    """A parent class for representation of denary numbers"""

    def convert_to_fractional(self):
        raise NotImplementedError

    def convert_to_decimal(self):
        raise NotImplementedError

    def convert_to_binary_fraction(self):
        raise NotImplementedError


class FractionalNumber(DenaryNumber):
    """ """

    def __init__(self, numerator: int, denominator: int):
        self.is_positive = not ((numerator < 0) ^ (denominator < 0))
        self.numerator = abs(numerator)
        assert denominator != 0, "The denominator cannot be 0"
        self.denominator = abs(denominator)
        # self.bin_denominator = bin(self.denominator)
        # self.bin_denominator_subtracted = bin(self.denominator - 1)

    # def is_den_power_of_2(self):


class DecimalNumber(DenaryNumber):
    """ """

    def __init__(self, decimal_number: float):
        self.decimal_number = decimal_number
        self.is_positive = decimal_number > 0
        self.int_part = int(self.decimal_number)
        self.decimal_part = abs(self.decimal_number) - abs(self.int_part)
