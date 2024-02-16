# instance_management.py

from models.ieee_format import IEEEFormat, IEEE16BitFormat, IEEE32BitFormat, IEEE64BitFormat, IEEECustomLengthFormat
from models.binary_number import BinaryNumber
from models.denary_number import DenaryNumber, FractionalNumber, DecimalNumber
from models.ieee_float import IEEEfloat
from models.number_representation import NumberRepresentation

class InstanceManagement:
    
    
    def create_ieee_format_instance(self, format_type="custom_length", **kwargs):
        if format_type == "16bit":
            return IEEE16BitFormat(**kwargs)
        elif format_type == "32bit":
            return IEEE32BitFormat(**kwargs)
        elif format_type == "64bit":
            return IEEE64BitFormat(**kwargs)
        else:
            return IEEECustomLengthFormat(**kwargs)
    
    def create_number_representation_instance(self, ieee_format=None, binary_number=None, denary_number=None, ieee_float=None):
        return NumberRepresentation(ieee_format=ieee_format, binary_number=binary_number, denary_number=denary_number)
    
    def create_binary_number_instance(self, binary_whole_part, binary_fraction, is_positive):
        return BinaryNumber(binary_whole_part=binary_whole_part, binary_fraction=binary_fraction, is_positive=is_positive)
    
    def create_fractional_number(self, numerator, denominator):
        return FractionalNumber(numerator=numerator, denominator=denominator)
    
    def create_decimal_number(self, decimal_number):
        return DecimalNumber(decimal_number)
    
    def create_denary_number(self, denary_fraction=None, denary_decimal=None):
        return DenaryNumber
    
    def create_ieee_float(
        self,
        ieee_format,
        sign_bit,
        exponent,
        calculated_exponent,
        mantissa,
        is_precise,
        ):
        return IEEEfloat(
        ieee_format=ieee_format,
        sign_bit=sign_bit,
        exponent=exponent,
        calculated_exponent=calculated_exponent,
        mantissa=mantissa,
        is_precise=is_precise,
        )