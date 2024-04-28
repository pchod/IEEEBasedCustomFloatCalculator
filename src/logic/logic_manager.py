# logic_manager.py

import json
from binary_operations import BinaryOperations
from instance_management import InstanceManagement

class LogicManager:
    """Orchestrating the logic flow of the calculator"""

    def __init__(self):
        self.instance_manager = InstanceManagement()
        self.binary_operations = BinaryOperations()

    def convert_fractional_to_IEEE_float(self, numerator, denominator):
        pass
    """
    def convert_denary_fraction_to_IEEE_float_normal_num(self, input_data):
        Working on seperate arguments instead of class objects - need to change, when the functions work properly
        numerator_bin, denominator_bin = BinaryOperations.convert_int_to_binary(simplified_numerator), BinaryOperations.convert_int_to_binary(simplified_denominator)
        print(f"execution suite: {simplified_numerator}: {numerator_bin}, {simplified_denominator}: {denominator_bin}")
        whole_part_bin, remainder_after_whole_part = BinaryOperations.convert_to_binary_fraction_whole_part(numerator_bin, denominator_bin)
        is_whole_part_zero = BinaryOperations.is_whole_part_zero(whole_part_bin)
        fractional_part_bin, complete_division = BinaryOperations.convert_to_binary_fraction_fraction_part(remainder_after_whole_part, denominator_bin, is_whole_part_zero, ieee_format)
        normalized_fractional_part_bin, left_shifts, right_shifts = BinaryOperations.normalise_binary_fraction(whole_part_bin, fractional_part_bin)
        normalized_fractional_part_bin = BinaryOperations.remove_leading_1(normalized_fractional_part_bin)
        exponent_int = BinaryOperations.calculate_normalized_exponent_int(left_shifts, right_shifts, ieee_format)
        print(f"print statement inside the code execution suite {exponent_int}")
        den_is_power_of_2 = DenaryNumber._is_den_power_of_2()
        print(f"Is denominator power of 2: {den_is_power_of_2}")
        need_to_round = BinaryOperations.need_to_round(normalized_fractional_part_bin, ieee_format, den_is_power_of_2)
        if need_to_round:
            normalized_fractional_part_bin = BinaryOperations.round_the_normalized_fractional_part(normalized_fractional_part_bin, ieee_format, den_is_power_of_2)
        sign_bit, exponent, mantissa = BinaryOperations.calculate_IEEE_float(is_positive, exponent_int, normalized_fractional_part_bin, ieee_format)
        print(f"Length of sign bit: {len(sign_bit)}, length of exponent: {len(exponent)}, length of mantissa: {len(mantissa)}. Was the number rounded? {need_to_round}")
        return (sign_bit, exponent, mantissa)
    """