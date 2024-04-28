# denary_number.py


from models.ieee_format import IEEEFormat


class DenaryNumber:
    """A parent class for representation of denary numbers"""

    def _gcd(self, num=None, den=None):
        if num == None:
            numerator = self.numerator
        else:
            numerator = num
        if den == None:
            denominator = self.denominator
        else:
            denominator = den
        gcd = 0
        while denominator:
            gcd = denominator
            denominator = numerator % denominator
            numerator = gcd
        return gcd

    def _simplify_fraction(self, num=None, den=None):
        """Using floor division to prevent getting float as a result. GCD is used to simplify the fraction"""
        if num == None:
            simplified_numerator = self.numerator
        else:
            simplified_numerator = num
        if den == None:
            simplified_denominator = self.denominator
        else:
            simplified_denominator = den
        if simplified_denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        gcd = self._gcd(num=simplified_numerator, den=simplified_denominator)
        simplified_numerator //= gcd
        simplified_denominator //= gcd
        return simplified_numerator, simplified_denominator

    def _is_den_power_of_2(self, denominator=None):
        """Using bitwise operation to determine if the denominator is a power of 2. Needed for sticky bit calculation in rounding process
        while converting to binary fraction and IEEE 754 format"""
        if denominator == None:
            if self.simplified_denominator == 0:
                raise ZeroDivisionError("The denominator cannot be 0")
            return True if self.simplified_denominator & (self.simplified_denominator - 1) == 0 else False
        if denominator:
            if denominator == 0:
                raise ZeroDivisionError("The denominator cannot be 0")
            return True if denominator & (denominator - 1) == 0 else False


class FractionalNumber(DenaryNumber):
    """ """

    def __init__(self, numerator: int, denominator=1):
        self.is_positive = not ((numerator < 0) ^ (denominator < 0))
        self.numerator = abs(numerator)
        assert denominator != 0, "The denominator cannot be 0"
        self.denominator = abs(denominator)
        self.simplified_numerator, self.simplified_denominator = self._simplify_fraction()
        self.den_is_power_of_2 = self._is_den_power_of_2()
        self.decimal_float = self._convert_to_decimal()

    def _convert_to_decimal(self):
        """Returns int"""
        decimal_float = self.numerator / self.denominator
        return decimal_float


class DecimalNumber(DenaryNumber):
    """Parameters should be passed as integers. Respectively both for int part and fractional part """

    def __init__(self, int_part, fract_part, is_positive=True):
        self.int_part = int_part
        self.fractional_part = abs(fract_part)
        self.simplified_fractional_part = int(str(self.fractional_part).lstrip("0"))
        self.is_positive = is_positive if int_part >= 0 else False
        self.is_decimal_zero = self.int_part == 0 and self.simplified_fractional_part == 0
        self.numerator, self.denominator = self._convert_to_fractional()
        self.den_is_power_of_2 = self._is_den_power_of_2()

    def _convert_to_fractional(self):
        """Returns a tuple numerator, denominator"""
        if self.is_decimal_zero:
            return 0, 1
        elif self.simplified_fractional_part == 0:
            return self.int_part, 1
        else:
            denominator = int(10 * len(str(self.simplified_fractional_part)))
            numerator = self.int_part * denominator + self.simplified_fractional_part
            return self._simplify_fraction(numerator, denominator)
