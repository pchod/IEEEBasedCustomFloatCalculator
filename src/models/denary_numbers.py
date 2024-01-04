# denary_numbers.py


class FractionalNumber:
    """ """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        # self.bin_denominator = bin(self.denominator)
        # self.bin_denominator_subtracted = bin(self.denominator - 1)

    # def to_binary(self):

    # def is_den_power_of_2(self):


class DecimalNumber:
    """ """

    def __init__(self, decimal_number):
        self.decimal_number = decimal_number
        self.int_part = int(self.decimal_number)
        # bool for sign

        # needs to add abs() self.fractional_part = self.decimal_number - self.int_part
