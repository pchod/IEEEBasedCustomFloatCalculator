# denary_number.py


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
        self.numerator, self.denominator = numerator, denominator
        self.den_is_power_of_2 = self._is_den_power_of_2(self.denominator)
        self.decimal_float_derived = self.numerator / self.denominator


class DecimalNumber(DenaryNumber):
    """ """

    def __init__(self, int_part: int, fract_part: int, scale_factor: int,  is_positive=True):
        self.int_part = int_part
        self.fractional_part = fract_part
        self.scale_factor = scale_factor
        self.is_positive = is_positive
        self.decimal_number = f"{int_part}.{fract_part}"
        self.is_decimal_zero = True if int_part == 0 and fract_part == 0 else False
        # self.numerator_derived, self.denominator_derived = self._convert_to_fractional()
        # self.den_derived_is_power_of_2 = self._is_den_power_of_2(self.denominator_derived)
