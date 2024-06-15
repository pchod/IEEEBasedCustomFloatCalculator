# denary_number.py

from models.ieee_format import IEEEFormat


class DenaryNumber:
    """A parent class for representation of denary numbers"""

    def _simplify_fraction(self, numerator, denominator):
        """Using floor division to prevent getting float as a result. GCD is used to simplify the fraction"""
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        gcd = self._get_gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        return numerator, denominator

    def _get_gcd(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        gcd = 0
        while denominator:
            gcd = denominator
            denominator = numerator % denominator
            numerator = gcd
        return gcd

    def _is_den_power_of_2(self, denominator):
        """Using bitwise operation to determine if the denominator is a power of 2.
        Needed for sticky bit calculation in rounding process
        while converting to binary fraction and IEEE 754 format."""
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        return True if denominator & (denominator - 1) == 0 else False


class FractionalNumber(DenaryNumber):
    """ """

    def __init__(self, numerator: int, denominator=1, is_positive=True):
        self.is_positive = is_positive
        assert denominator != 0, "The denominator cannot be 0"
        self.numerator_entered, self.denominator_entered = numerator, denominator
        self.numerator, self.denominator = self._simplify_fraction(numerator, denominator)
        self.den_is_power_of_2 = self._is_den_power_of_2(self.denominator)
        self.decimal_float_derived = self._convert_to_decimal()

    def _convert_to_decimal(self):
        """Returns decimal float representation of the fractional number"""
        decimal_float = self.numerator / self.denominator
        return decimal_float


class DecimalNumber(DenaryNumber):
    """ """

    def __init__(self, int_part: str, fract_part: str, is_positive=True):
        self.int_part = int_part
        self.fractional_part = fract_part
        self.is_positive = is_positive
        self.decimal_number = f"{int_part}.{fract_part}"
        self.is_decimal_zero = True if all(char == '0' for char in int_part) and all(char == '0' for char in fract_part) else False
        self.numerator_derived, self.denominator_derived = self._convert_to_fractional()
        self.den_derived_is_power_of_2 = self._is_den_power_of_2(self.denominator_derived)

# NEEDS CHANGE - TO WORK ONLY ON STRINGS PASSED
    def _convert_to_fractional(self):
        """Returns a tuple numerator, denominator"""
        if self.is_decimal_zero:
            return 0, 1
        elif self.fractional_part == 0:
            return self.int_part, 1
        else:
            fract_part_str = str(self.fractional_part).split(".")[1]
            denominator = 10 ** len(fract_part_str)
            numerator = int(fract_part_str) + self.int_part * denominator
            return self._simplify_fraction(numerator, denominator)
