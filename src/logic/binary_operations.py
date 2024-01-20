# binary_operations.py

from pprint import pprint

from icecream import ic

from models.ieee_format import IEEEFormat


class BinaryOperations:
    @staticmethod
    def check_underflow(ieee_underflow_value, number):
        """Returns a bool for underflow check. True, if the number is in the underflow range"""
        return -(ieee_underflow_value) < number < ieee_underflow_value

    @staticmethod
    def check_overflow(ieee_overflow_value, number):
        """Returns a bool for overflow check. True, if the number is above the overflow ranges"""
        return number < -(ieee_overflow_value) or number > ieee_overflow_value

    @staticmethod
    def check_special_cases():
        pass

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
    def subtract_binaries(binary_1: str, binary_2: str):
        """Subtracting binary_1 - binary_2 using bitwise operations. It is guaranteed, that binary_1 > binary_2 - need to add the check"""
        # ic(binary_1, binary_2)
        subtraction_product = []
        borrow = False

        # performing subtraction from right to left
        for index in range((len(binary_1) - 1), -1, -1):
            # ic(subtraction_product)
            bit_binary_1 = binary_1[index]
            bit_binary_2 = binary_2[index]
            # print()
            # print("state before subtraction, checking remaining borrow based on the previous iteration")
            # ic(bit_binary_1, bit_binary_2, borrow)
            # print()
            # print("state after checking borrow")
            # ic(bit_binary_1, bit_binary_2, borrow)
            # print()
            # print("starting subtraction")
            # ic(bit_binary_1, bit_binary_2, borrow)
            # checked and correct
            if bit_binary_1 < bit_binary_2:
                # print("bit 1 is lower than bit 2")
                borrow = True
                # ic(borrow)

                subtraction_product.append("1")

            elif bit_binary_1 > bit_binary_2:
                subtraction_product.append("0" if borrow else "1")
                # print("bit 1 is higher than bit 2")
                if borrow:
                    borrow = False

            else:
                # for equal bits the product is 0, if the bit is borrowed, be become 1
                # print("bit 1 is equal to bit 2")
                subtraction_product.append("1" if borrow else "0")
                borrow = (bit_binary_1 == "0") and borrow
        # ic(subtraction_product)
        subtraction_product_reversed = reversed(subtraction_product)
        subtraction_product_bin = "".join(subtraction_product_reversed)
        # ic(subtraction_product_bin)
        return subtraction_product_bin

    """@staticmethod
    def perform_long_division(numerator_bin: str, denominator_bin: str, precision: None):
        Implementation of a long division for binaries. Returns the whole part and the remainder. Serves as a helper
        function for binary whole part and fractional part conversion
        
        division_product = ""
        for i, bit in enumerate(numerator_bin):
            remainder_bin += bit
            ic(bit, remainder_bin, denominator_bin, whole_part_bin)
            padded_remainder, padded_denominator = BinaryOperations.left_zero_pad_shorter_bin(
                remainder_bin, denominator_bin
            )
            
            if padded_remainder >= padded_denominator:
            
                #remainder_bin, denominator_bin = (
                #    BinaryOperations.left_zero_pad_shorter_bin(
                #        remainder_bin, denominator_part
                #    )
                #)
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

        return """
    @staticmethod

    def convert_int_to_binary(number: int):
        """Converts an integer to binary using string concatenation. Returns a string"""
        binary = ""
        if number == 0:
            return "0"
        while number > 0:
            binary = str(number % 2) + binary
            number = number // 2
            return binary
    
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
        numerator_bin = numerator_bin.lstrip("0")
        if not numerator_bin:
            numerator_bin = "0"
        # need for thoroygh testing
        if not denominator_bin:
            raise ValueError("Cannot divide by zero")
        denominator_bin = denominator_bin.lstrip("0")
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
        ic(
            remainder_after_whole_part,
            denominator_bin,
            is_whole_part_zero,
            ieee_format.mantissa_length,
        )
        if not remainder_after_whole_part or remainder_after_whole_part == "0":
            return "0"
        remainder_bin = ""
        padded_current_remainder = ""
        padded_denominator = ""
        denominator_bin = denominator_bin.lstrip("0")
        fractional_part_bin = ""
        i = 0
        digits_after_first_1 = 0
        first_1_found = not is_whole_part_zero
        while (
            (
                is_whole_part_zero
                and len(fractional_part_bin)
                < (
                    ieee_format.max_left_shifts
                    + ieee_format.exponent_length
                    + ieee_format.mantissa_length
                    + 1
                )
            )
            or (
                not first_1_found
                and len(fractional_part_bin)
                < (
                    ieee_format.max_left_shifts
                    + ieee_format.exponent_length
                    + ieee_format.mantissa_length
                    + 1
                )
            )
            or (
                first_1_found
                and digits_after_first_1
                < (
                    ieee_format.max_left_shifts
                    + ieee_format.exponent_length
                    + ieee_format.mantissa_length
                    + 1
                )
            )
        ):
            if i < len(remainder_after_whole_part):
                bit = remainder_after_whole_part[i]
            else:
                bit = "0"
            remainder_bin += bit
            ic(bit, remainder_bin, denominator_bin)
            padded_current_remainder, padded_denominator = (
                BinaryOperations.left_zero_pad_shorter_bin(
                    remainder_bin, denominator_bin
                )
            )

            if padded_current_remainder >= padded_denominator:
                # remainder_bin, denominator_bin = (
                #    BinaryOperations.left_zero_pad_shorter_bin(
                #        remainder_bin, denominator_part
                #    )
                # )
                ic(remainder_bin, padded_denominator)
                remainder_bin = BinaryOperations.subtract_binaries(
                    padded_current_remainder, padded_denominator
                )
                print()
                print("after subtraction")
                fractional_part_bin += "1"
                ic(remainder_bin, padded_denominator, fractional_part_bin)
                print()
                if not first_1_found:
                    first_1_found = True
                else:
                    digits_after_first_1 += 1
            else:
                fractional_part_bin += "0"
                if first_1_found:
                    digits_after_first_1 += 1
            i += 1
        ic(
            fractional_part_bin,
            padded_current_remainder,
            padded_denominator,
            first_1_found,
        )
        print(
            f"the IEEE length of mantissa is {ieee_format.mantissa_length},"
            f" while the actual length is {len(fractional_part_bin)}"
        )
        return fractional_part_bin

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
        else:
            return True

    @staticmethod
    def normalise_binary_fraction(
        whole_part_bin: str,
        fractional_part_bin: str,
    ):
        """Used for normal numbers to convert to IEEE. need to add function for checking the normalisation range
        NEED TO ADD TRY/EXCEPT FOR STRING TYPES AND CALCULATING THE EXPONENT AND MANTISSA
        """

        right_shifts = 0
        left_shifts = 0
        # converting whole_part_bin into list

        whole_part_bin = list(whole_part_bin) if whole_part_bin else []
        if whole_part_bin:
            right_shifts = len(whole_part_bin)
            normalized_fractional_part_bin = list(fractional_part_bin)
            for digit in whole_part_bin[:-1]:
                normalized_fractional_part_bin.insert(0, digit)
            normalized_fractional_part_bin = "".join(
                normalized_fractional_part_bin
            )
        elif not whole_part_bin and set(fractional_part_bin) == {"0"}:
            normalized_fractional_part_bin = fractional_part_bin
            right_shifts = 0
        else:
            normalized_fractional_part_bin = fractional_part_bin.lstrip(0)
            left_shifts = len(fractional_part_bin) - len(
                normalized_fractional_part_bin
            )

        return normalized_fractional_part_bin, left_shifts, right_shifts

    @staticmethod
    def remove_trailing_1(normalized_fractional_part_bin):
        return normalized_fractional_part_bin[1:] if normalized_fractional_part_bin[0] == "1" else normalized_fractional_part_bin
    
    @staticmethod
    def calculate_normalized_exponent_int(left_shifts, right_shifts, ieee_format):
        return ieee_format.exponent_bias + right_shifts if right_shifts > 0 else ieee_format.exponent_bias - left_shifts
    
    @staticmethod
    def calculate_bin_exponent(exponent_int, ieee_format):
        if exponent_int == 0:
            return "0" * ieee_format.exponent_length
        elif exponent_int < 0:
            raise ValueError("The exponent cannot be negative")
        else:
            calculated_bin_exponent = BinaryOperations.convert_int_to_binary(exponent_int)
            if len(calculated_bin_exponent) < ieee_format.exponent_length:
                calculated_bin_exponent = "0" * (ieee_format.exponent_length - len(calculated_bin_exponent)) + calculated_bin_exponent
                return calculated_bin_exponent
            
    def need_to_round(normalized_fractional_part_bin, ieee_format):
        """Checks if the normalized fractional part needs to be rounded. The normalized fractional part has to be passed without the leading 1"""
        if len(normalized_fractional_part_bin) < ieee_format.mantissa_length:
            return False
        elif normalized_fractional_part_bin[ieee_format.mantissa_length + 1] == "1":
            return True
        else:   
            return False
        
    def round_the_normalized_fractional_part(normalized_fractional_part_bin, ieee_format):
        """Rounds the normalized fractional part. The normalized fractional part has to be passed without the leading 1"""
        if len(normalized_fractional_part_bin) < ieee_format.mantissa_length:
            return normalized_fractional_part_bin
        


    @staticmethod
    def calculate_IEEE_float(is_positive: bool, calculated_bin_exponent: str, normalized_fractional_part: str, ieee_format: IEEEFormat):
        sign_bit = "0" if is_positive else "1"
        normalized_fractional_part = remove_trailing_1(normalized_fractional_part)
        
        exponent = convert_int_to_binary(exponent)

        
        
        return (sign_bit, exponent, mantissa)

    @staticmethod
    def convert_from_normalized_binary_fraction_to_IEEE_float():
        pass

    @staticmethod
    def convert_from_IEEE_to_binary_fraction():
        pass

    @staticmethod
    def convert_from_binary_fraction_to_denary():
        pass
