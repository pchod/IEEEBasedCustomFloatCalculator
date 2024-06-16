# binary_operations.py

from pprint import pprint

from icecream import ic

from backend.app.models.ieee_format import IEEEFormat
from backend.app.models.denary_number import DenaryNumber


class BinaryOperations:
    
    @staticmethod
    def check_underflow(ieee_underflow_value, number):
        """Returns a bool for underflow check. True, if the number is in the underflow range"""
        return -ieee_underflow_value < number < ieee_underflow_value

    @staticmethod
    def check_overflow(ieee_overflow_value, number):
        """Returns a bool for overflow check. True, if the number is above the overflow ranges"""
        return number < -ieee_overflow_value or number > ieee_overflow_value

    @staticmethod
    def check_special_cases():
        pass

    @staticmethod
    def compare_binaries(bin1: str, bin2: str) -> int:
        """Compare two binary strings lexicographically"""
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        if bin1 < bin2:
            return -1
        elif bin1 == bin2:
            return 0
        else:
            return 1

    @staticmethod
    def compare_bin_lengths(binary_1: str, binary_2: str):
        if len(binary_1) > len(binary_2):
            return 1
        elif len(binary_2) > len(binary_1):
            return -1

        else:
            return 0

    @staticmethod
    def left_zero_pad_shorter_bin(binary_1: str, binary_2: str):
        left_padding = ""
        comparision = BinaryOperations.compare_bin_lengths(binary_1, binary_2)
        if comparision == 0:
            return binary_1, binary_2

        elif comparision == 1:
            left_padding = "0" * (len(binary_1) - len(binary_2))
            binary_2 = left_padding + binary_2
            return binary_1, binary_2
        else:
            left_padding = "0" * (len(binary_2) - len(binary_1))
            binary_1 = left_padding + binary_1
            return binary_1, binary_2

    @staticmethod
    def right_zero_pad(fraction_part_bin: str, ieee_format: IEEEFormat):
        """Padding with zeros on the right to prepare for the fraction division with given precision"""
        while len(fraction_part_bin) < ieee_format.mantissa_length:
            fraction_part_bin += "0"
        return fraction_part_bin

    @staticmethod
    def subtract_binaries(bin1: str, bin2: str) -> str:
        """Subtract binary_2 from binary_1. Assumes binary_1 >= binary_2."""
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)
        bin2 = bin2.zfill(max_len)

        result = []
        borrow = False

        for i in range(max_len - 1, -1, -1):
            bit1 = bin1[i]
            bit2 = bin2[i]

            if borrow:
                if bit1 == '1':
                    bit1 = '0'
                    borrow = False
                else:
                    bit1 = '1'
                    borrow = True

            if bit1 == '0' and bit2 == '1':
                borrow = True
                result.append('1')
            elif bit1 == bit2:
                result.append('0')
            else:
                result.append('1')

        # Remove leading zeros and return result
        result.reverse()
        result = ''.join(result).lstrip('0')
        return result or '0'

    @staticmethod
    def convert_int_to_binary(number: int) -> str:
        """Converts an integer to binary using string concatenation. Returns a string"""
        print(f"Converting {number} to binary")
        if number == 0:
            print("Number is 0, returning '0'")
            return "0"
        binary = ""
        while number > 0:
            print(f"Current number: {number}, current binary: {binary}")
            binary = str(number % 2) + binary
            number = number // 2
        print(f"Final binary representation of {number}: {binary}")
        return binary

    @staticmethod
    def new_whole_part_long_division(num_bin: str, den_bin: str):
        """
        Performed only if num > den.
        Returns:
            Whole part bin
            Remainder for the fractional division.
        """

        def _long_division_whole(remainder, divisor, whole_part_bin, index):
            if index == len(num_bin):
                return whole_part_bin, remainder

            # Shift the remainder by adding the next bit of the numerator
            remainder += num_bin[index]
            remainder = remainder.lstrip('0') or '0'

            padded_remainder, padded_denominator = BinaryOperations.left_zero_pad_shorter_bin(remainder, divisor)
            comparison_result = BinaryOperations.compare_binaries(padded_remainder, padded_denominator)

            if comparison_result >= 0:
                whole_part_bin.append("1")
                remainder = BinaryOperations.subtract_binaries(padded_remainder, padded_denominator)
            else:
                whole_part_bin.append("0")

            return _long_division_whole(remainder, divisor, whole_part_bin, index + 1)

        if len(num_bin) < len(den_bin):
            return "0", num_bin
        elif num_bin == den_bin:
            return "1", "0"
        else:
            whole_part_bin = []
            quotient, remainder = _long_division_whole("", den_bin, whole_part_bin, 0)
            quotient = ''.join(quotient).lstrip("0") or "0"
            return quotient, remainder

    @staticmethod
    def convert_to_binary_fraction_whole_part(
        numerator_bin: str, denominator_bin: str
    ):
        """Performing a division to get the whole part of the binary fraction. Returns the whole part
        and the remainder for the further division for fractional part"""
        print()
        print("new division")
        print()
        ic(numerator_bin, denominator_bin)
        #numerator_bin = numerator_bin.lstrip("0")
        if not numerator_bin:
            numerator_bin = "0"
        # need for thoroygh testing
        if not denominator_bin:
            raise ValueError("Cannot divide by zero")
        # denominator_bin = denominator_bin.lstrip("0")
        ic(numerator_bin, denominator_bin)
        whole_part_bin = ""
        remainder_bin = ""

        for i, bit in enumerate(numerator_bin):
            remainder_bin += bit
            ic(bit, remainder_bin, denominator_bin, whole_part_bin)
            padded_remainder, padded_denominator = (
                BinaryOperations.left_zero_pad_shorter_bin(
                    remainder_bin, denominator_bin
                )
            )

            if padded_remainder >= padded_denominator:
                # remainder_bin, denominator_bin = (
                #    BinaryOperations.left_zero_pad_shorter_bin(
                #        remainder_bin, denominator_part
                #    )
                # )
                ic(remainder_bin, padded_denominator)
                remainder_bin = BinaryOperations.subtract_binaries(
                    padded_remainder, padded_denominator
                )
                print()
                print("after subtraction")
                whole_part_bin += "1"
                ic(remainder_bin, padded_denominator, whole_part_bin)
                print()
            else:
                whole_part_bin += "0"
        ic(remainder_bin, padded_denominator)
        whole_part_bin = whole_part_bin.lstrip("0")
        if not whole_part_bin:
            whole_part_bin = "0"
        ic(whole_part_bin, remainder_bin)
        return whole_part_bin, remainder_bin

    @staticmethod
    def is_whole_part_zero(whole_part_bin: str):
        "Used to check if the conversion to IEEE format will utilize left shifts. Returns True if the whole part is zero and no left shift is needed"
        return True if not "1" in whole_part_bin else False

    @staticmethod
    def convert_to_binary_fraction_fraction_part(
        remainder_after_whole_part: str,
        denominator_bin: str,
        is_whole_part_zero: bool,
        ieee_format: IEEEFormat,
    ):
        """Convert the remainder to a binary fraction part."""
        if not remainder_after_whole_part or set(remainder_after_whole_part) == {"0"}:
            return "0", True

        remainder_bin = remainder_after_whole_part
        fractional_part_bin = ""
        complete_division = False
        digits_after_first_1 = 0
        first_1_found = not is_whole_part_zero

        target_length = ieee_format.exponent_length + ieee_format.mantissa_length + 3
        if not is_whole_part_zero:
            target_length += ieee_format.max_left_shifts

        while len(fractional_part_bin) < target_length:
            remainder_bin += "0"
            remainder_bin = remainder_bin.lstrip("0") or "0"
            padded_remainder, padded_denominator = BinaryOperations.left_zero_pad_shorter_bin(remainder_bin, denominator_bin)

            if padded_remainder >= padded_denominator:
                fractional_part_bin += "1"
                remainder_bin = BinaryOperations.subtract_binaries(padded_remainder, padded_denominator)
                if not first_1_found:
                    first_1_found = True
                else:
                    digits_after_first_1 += 1
            else:
                fractional_part_bin += "0"

            if first_1_found:
                digits_after_first_1 += 1

            if set(remainder_bin) == {"0"}:
                complete_division = True
                break

        return fractional_part_bin, complete_division

    # def round_binary_fraction_part(fractional_part_bin: str, ieee_format: IEEEFormat):
    #    """"""
    #    is_rounded = False
    #    if not fractional_part_bin or fractional_part_bin == "0":
    #        fractional_part_bin = "0" * ieee_format.mantissa_length
    #        return fractional_part_bin, is_rounded = False
    #    if len(fractional_part_bin) > ieee_format.mantissa_length:
    #        fractional_part_bin = fractional_part_bin[:ieee_format.mantissa_length + 2]
    #        if fractional_part_bin[-1] == "1" and fractional_part_bin[-2] == "0":
    #            fractional_part_bin = fractional_part_bin[:-2] + "1"
    #            is_rounded = True
    #        else:
    #           fractional_part_bin = fractional_part_bin[:-1]
    #            is_rounded = False

    # seems reduntant with the is_whole_part_zero function - needs to check
    @staticmethod
    def check_need_to_normalise(
        whole_part_bin: str, fractional_part_bin: str, ieee_format: IEEEFormat
    ):
        """Needs to add the parameter and conditions for subnormal numbers and special cases."""
        whole_part_bin = whole_part_bin.lstrip("0")
        if not whole_part_bin and fractional_part_bin[0] == "1":
            return False
        
        elif whole_part_bin and len(whole_part_bin) == 1:
            return False
        
        else:
            return True

    @staticmethod
    def normalise_binary_fraction(whole_part_bin: str, fractional_part_bin: str):
        """Normalize the binary fraction and calculate shifts."""
        right_shifts = 0
        left_shifts = 0

        # Strip leading zeros from the whole part
        whole_part_bin = whole_part_bin.lstrip("0")

        # Check if the whole part exists and normalize accordingly
        if whole_part_bin:
            # Whole part exists, calculate right shifts
            right_shifts = len(whole_part_bin) - 1
            normalized_fractional_part_bin = whole_part_bin + fractional_part_bin
        else:
            # No whole part, normalize the fractional part
            first_one_index = fractional_part_bin.find('1')
            if first_one_index != -1:
                # The number of left shifts is the position of the first '1' in the fractional part
                left_shifts = first_one_index + 1
                normalized_fractional_part_bin = fractional_part_bin[first_one_index + 1:]
            else:
                normalized_fractional_part_bin = "0"
                left_shifts = 0

        return normalized_fractional_part_bin, left_shifts, right_shifts

    @staticmethod
    def remove_leading_1(normalized_fractional_part_bin):
        print("debug: normalized fractional part 2 first digits before removing leading 1", normalized_fractional_part_bin[0:1])
        return normalized_fractional_part_bin[1:] if normalized_fractional_part_bin[0] == "1" else normalized_fractional_part_bin
    
    @staticmethod
    def calculate_normalized_exponent_int(left_shifts, right_shifts, ieee_format):
        bias = ieee_format.bias
        # Adjust the exponent based on the number of shifts
        if right_shifts > 0:
            calculated_exponent = bias + right_shifts
        else:
            calculated_exponent = bias - left_shifts
        return calculated_exponent
    
    @staticmethod
    def calculate_bin_exponent(exponent_int: int, ieee_format):
        print(f"print statement inside the function calculate_bin_exponent {exponent_int}")
        bias = ieee_format.bias
        biased_exponent = exponent_int

        if biased_exponent == 0:
            print("exponent is 0")
            return "0" * ieee_format.exponent_length
        elif biased_exponent < 0:
            print("exponent is negative")
            raise ValueError("The biased exponent cannot be negative")
        else:
            calculated_bin_exponent = BinaryOperations.convert_int_to_binary(biased_exponent)
            print(f"Calculated binary exponent: {calculated_bin_exponent}")
            if len(calculated_bin_exponent) < ieee_format.exponent_length:
                calculated_bin_exponent = "0" * (ieee_format.exponent_length - len(calculated_bin_exponent)) + calculated_bin_exponent
                return calculated_bin_exponent
            elif len(calculated_bin_exponent) == ieee_format.exponent_length:
                return calculated_bin_exponent
            else:
                raise ValueError("Calculated exponent exceeds allowable length")

    @staticmethod
    def need_to_round(normalized_fractional_part_bin, ieee_format: IEEEFormat, den_is_power_of_2: bool):
        """Checks if the normalized fractional part needs to be rounded. The normalized fractional part has to be passed without the leading 1.
        The rule for rounding is round to nearest, tie to even. The function returns True if the rounding is needed and False if not."""

        print("debug: first digit of the normalized fractional part", normalized_fractional_part_bin[0])
        if len(normalized_fractional_part_bin) < ieee_format.mantissa_length:
            return False
        normalized_fractional_part_bin = list(normalized_fractional_part_bin)

        # Ensure enough length for accessing indices
        if len(normalized_fractional_part_bin) < ieee_format.mantissa_length + 2:
            return False

        lsb = normalized_fractional_part_bin[ieee_format.mantissa_length - 1]
        guard_bit = normalized_fractional_part_bin[ieee_format.mantissa_length]
        rounding_bit = normalized_fractional_part_bin[ieee_format.mantissa_length + 1]
        sticky_bit = "1" if not den_is_power_of_2 else "0"

        if lsb == "1":
            return False

        if lsb == "0":
            if guard_bit and rounding_bit and sticky_bit == "0":
                return False
            elif guard_bit == "1":
                return True
            elif guard_bit == "0" and (rounding_bit or sticky_bit) == "1":
                return True

    @staticmethod
    def round_the_normalized_fractional_part(normalized_fractional_part_bin, ieee_format: IEEEFormat,
                                             den_is_power_of_2: bool):
        """Rounding the normalized fractional part. It is assumed that the normalized fractional part is passed without the leading 1.
        The function returns the rounded normalized fractional part. It's assumed, that LSB is 1 (based on the need_to_round function).
        The rounding is performed based on the LSB, guard bit, rounding bit and sticky bit."""
        normalized_fractional_part_bin = list(normalized_fractional_part_bin)

        # Ensure enough length for accessing indices
        if len(normalized_fractional_part_bin) < ieee_format.mantissa_length + 2:
            return ''.join(normalized_fractional_part_bin)

        lsb = normalized_fractional_part_bin[ieee_format.mantissa_length - 1]
        guard_bit = normalized_fractional_part_bin[ieee_format.mantissa_length]
        rounding_bit = normalized_fractional_part_bin[ieee_format.mantissa_length + 1]
        sticky_bit = "1" if not den_is_power_of_2 else "0"

        if guard_bit == "0" and rounding_bit == "0":
            lsb = "0"
        elif guard_bit == "0" and rounding_bit == "1":
            lsb = "1"
        elif guard_bit == "1" and rounding_bit == "0":
            lsb = "0"
        elif guard_bit == "1" and rounding_bit == "1":
            if sticky_bit == "1":
                lsb = "1"
            else:
                lsb = "0"

        normalized_fractional_part_bin[ieee_format.mantissa_length - 1] = lsb
        return "".join(normalized_fractional_part_bin)

    @staticmethod
    def calculate_IEEE_float(is_positive: bool, exponent: int, normalized_fractional_part: str, ieee_format: IEEEFormat):
        """Needs to the parameter of normalized fractional part without the leading 1 and rounded, if it was needed"""
        sign_bit = "0" if is_positive else "1"
        exponent = BinaryOperations.calculate_bin_exponent(exponent, ieee_format)
        if len(normalized_fractional_part) < ieee_format.mantissa_length:
            normalized_fractional_part = BinaryOperations.right_zero_pad(normalized_fractional_part, ieee_format)
        elif len(normalized_fractional_part) > ieee_format.mantissa_length:
            normalized_fractional_part = normalized_fractional_part[:ieee_format.mantissa_length]
        mantissa = normalized_fractional_part
        
        return (sign_bit, exponent, mantissa)

    @staticmethod
    def convert_denary_fraction_to_IEEE_float_normal_num(simplified_numerator: int, simplified_denominator: int, ieee_format: IEEEFormat, den_is_power_of_2: bool, is_positive: bool):
        """Working on seperate arguments instead of class objects - need to change, when the functions work properly"""
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

    @staticmethod
    def convert_from_IEEE_to_binary_fraction():
        pass

    @staticmethod
    def convert_from_binary_fraction_to_denary():
        pass