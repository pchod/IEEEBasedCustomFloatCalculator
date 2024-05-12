# instance_manager.py

from models.ieee_format import IEEEFormat, IEEE16BitFormat, IEEE32BitFormat, IEEE64BitFormat, IEEECustomLengthFormat
from models.binary_number import BinaryNumber
from models.denary_number import DenaryNumber, FractionalNumber, DecimalNumber
from models.ieee_float import IEEEfloat
from models.number_representation import NumberRepresentation

class InstanceManager:
    
    @staticmethod
    def create_ieee_format_instance(format_type="custom_length", **kwargs):
        if format_type == "16bit":
            return IEEE16BitFormat(**kwargs)
        elif format_type == "32bit":
            return IEEE32BitFormat(**kwargs)
        elif format_type == "64bit":
            return IEEE64BitFormat(**kwargs)
        else:
            return IEEECustomLengthFormat(**kwargs)

    @staticmethod
    def create_fractional_number_instance(**kwargs):
        return FractionalNumber(**kwargs)

    @staticmethod
    def create_decimal_number_instance(**kwargs):
        return DecimalNumber(**kwargs)

    @staticmethod
    def create_binary_number_instance(**kwargs):
        return BinaryNumber(**kwargs)
    @staticmethod
    def create_ieee_float(**kwargs):
        return IEEEfloat(**kwargs)

    @staticmethod
    def create_number_representation_instance(**kwargs):
        return NumberRepresentation(**kwargs)