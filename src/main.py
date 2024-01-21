from models.binary_number import BinaryNumber
from models.denary_number import FractionalNumber
from models.ieee_format import IEEEFormat, IEEE16BitFormat, IEEE32BitFormat, IEEE64BitFormat
from models.ieee_float import IEEEfloat
from logic.binary_operations import BinaryOperations

denary_fraction = FractionalNumber(1, 5)
ieee_format = IEEE32BitFormat()
print(denary_fraction.numerator, denary_fraction.denominator)
ieee_float = BinaryOperations.convert_denary_fraction_to_IEEE_float_normal_num(denary_fraction.simplified_numerator, denary_fraction.simplified_denominator, ieee_format, denary_fraction.den_is_power_of_2, denary_fraction.is_positive)

print(ieee_float)