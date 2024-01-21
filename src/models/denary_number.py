# denary_number.py


from models.ieee_format import IEEEFormat


class DenaryNumber:
    """A parent class for representation of denary numbers"""
    
    def __init__(self):
        self.is_positive = None
        self.numerator = None
        self.denominator = None
        self.simplified_numerator = None
        self.simplified_denominator = None
        self.int_part = None
        self.decimal_part = None
        self.decimal_from_fractional = None
        self.den_is_power_of_2 = None

    def convert_to_fractional(self):
        raise NotImplementedError

    def convert_to_decimal(self):
        raise NotImplementedError

    def convert_to_binary_fraction(self):
        raise NotImplementedError
    
    def gcd(self, numerator, denominator):
        gcd = 0
        while denominator:
            gcd = denominator
            denominator = numerator % denominator
            numerator = gcd
        return gcd
    
    def simplify_fraction(self, numerator, denominator):
        """Using floor division to prevent getting float as a result. GCD is used to simplify the fraction"""
        if denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        gcd = self.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        return numerator, denominator
    
    def is_den_power_of_2(self):
        """Using bitwise operation to determine if the denominator is a power of 2. Needed for sticky bit calculation in rounding process
        while converting to binary fraction and IEEE 754 format"""
        if self.denominator == 0:
            raise ZeroDivisionError("The denominator cannot be 0")
        
        return True if self.denominator & (self.denominator - 1) == 0 else False


class FractionalNumber(DenaryNumber):
    """ """

    def __init__(self, numerator: int, denominator: int):
        self.is_positive = not ((numerator < 0) ^ (denominator < 0))
        self.numerator = abs(numerator)
        assert denominator != 0, "The denominator cannot be 0"
        self.denominator = abs(denominator)
        self.simplified_numerator, self.simplified_denominator = self.simplify_fraction(self.numerator, self.denominator)
        self.den_is_power_of_2 = self.is_den_power_of_2()
    # def is_den_power_of_2(self):


class DecimalNumber(DenaryNumber):
    """ """

    def __init__(self, decimal_number: float):
        self.decimal_number = decimal_number
        self.is_positive = decimal_number > 0
        self.int_part = int(self.decimal_number)
        self.decimal_part = abs(self.decimal_number) - abs(self.int_part)
        self.decimal_from_fractional = None