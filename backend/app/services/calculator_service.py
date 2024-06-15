# calculator_service.py
from backend.app.models.denary_number import DenaryNumber, FractionalNumber, DecimalNumber
from backend.app.models.ieee_float import IEEEFloat
from backend.app.models.binary_number import BinaryNumber
from backend.app.models.ieee_format import IEEEFormat, IEEE16BitFormat, IEEE32BitFormat, IEEE64BitFormat, \
    IEEECustomLengthFormat
from backend.app.models.number_representation import NumberRepresentation


class CalculatorService:

    @staticmethod
    def calculate_ieee_from_fractional(fractional_number: FractionalNumber, ieee_format: IEEEFormat):
        binary_number = BinaryNumber(is_positive=fractional_number.is_positive)
        ieee_float = IEEEFloat(is_positive=fractional_number.is_positive)
        number_representation = NumberRepresentation(fractional_number=fractional_number, ieee_format=ieee_format,
                                                     ieee_float=ieee_float, binary_number=binary_number)

        #numerator_bin, denominator_bin = BinaryOperations.convert_int_to_binary(simplified_numerator),
        # BinaryOperations.convert_int_to_binary(simplified_denominator)