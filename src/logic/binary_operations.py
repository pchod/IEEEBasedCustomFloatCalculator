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
        ic(binary_1, binary_2)
        subtraction_product = []
        borrow = False

        # performing subtraction from right to left
        for index in range((len(binary_1) - 1), -1, -1):
            ic(subtraction_product)
            bit_binary_1 = binary_1[index]
            bit_binary_2 = binary_2[index]
            print()
            print("state before subtraction, checking remaining borrow based on the previous iteration")
            ic(bit_binary_1, bit_binary_2, borrow)
            #if borrow:
                # the borrowed bit is nullified succesfuly and borrow flag is set to false
            #    if bit_binary_1 == "1":
            #        bit_binary_1 = "0"
            #        ic(bit_binary_1)
            #        borrow = False
            #        ic(borrow)
            #    else:
            #        bit_binary_1 = "1"
            #        ic(bit_binary_1)
            #       ic(borrow)
                # keeping the borrow for the next iteration
                #else:
                #    bit_binary_1 = "1"
            print()
            print("state after checking borrow")
            ic(bit_binary_1, bit_binary_2, borrow)
            print()
            print("starting subtraction")
            ic(bit_binary_1, bit_binary_2, borrow)
            # checked and correct
            if bit_binary_1 < bit_binary_2:
                print("bit 1 is lower than bit 2")
                borrow = True
                ic(borrow)

                subtraction_product.append("1")

            elif bit_binary_1 > bit_binary_2:
                subtraction_product.append("0" if borrow else "1")
                print("bit 1 is higher than bit 2")
                if borrow:
                    borrow = False

            else:
                # for equal bits the product is 0, if the bit is borrowed, be become 1
                print("bit 1 is equal to bit 2")
                subtraction_product.append("1" if borrow else "0")
                borrow = (bit_binary_1 == "0") and borrow
        ic(subtraction_product)
        subtraction_product_reversed = reversed(subtraction_product)
        subtraction_product_bin = "".join(subtraction_product_reversed)
        ic(subtraction_product_bin)
        return subtraction_product_bin

    @staticmethod
    def convert_to_binary_fraction_whole_part(
        numerator_bin: str, denominator_bin: str
    ):
        """Performing a division to get the whole part of the binary fraction. Returns the whole part
        and the remainder for the further division for fractional part"""
        numerator_bin = numerator_bin.lstrip("0")
        denominator_bin = denominator_bin.lstrip("0")
        whole_part_bin = ""
        remainder_bin = ""

        for bit in numerator_bin:
            remainder_bin += bit
            if remainder_bin >= denominator_bin:
                whole_part_bin += "1"
                remainder_bin, denominator_bin = (
                    BinaryOperations.left_zero_pad_shorter_bin(
                        remainder_bin, denominator_bin
                    )
                )
                ic(remainder_bin, denominator_bin)
                remainder_bin = BinaryOperations.subtract_binaries(
                    remainder_bin, denominator_bin
                )
                ic(remainder_bin, denominator_bin)
            else:
                whole_part_bin += "0"
        ic(remainder_bin, denominator_bin)
        whole_part_bin = whole_part_bin.lstrip("0")
        ic(whole_part_bin)
        return whole_part_bin, remainder_bin

    """
    @staticmethod
    def convert_to_binary_fraction_fraction_part(
        numerator_bin: str,
        remainder_after_whole_part: str,
        ieee_format: IEEEFormat,
    ):
        pass
    
        ic(numerator_bin, remainder_after_whole_part, ieee_format)
        pprint(ieee_format)
        if not remainder_after_whole_part:
            return "0"
        numerator_bin = numerator_bin.lstrip("0")
        remainder_after_whole_part += BinaryOperations.right_zero_pad(
            remainder_after_whole_part, ieee_format
        )
        ic(numerator_bin, remainder_after_whole_part)
        fractional_part_bin = ""
        temp_remainder = ""
        is_rounded = False
        # division until reaches
        # needs optimization in the next iteration - when the division is complete to pad with zeros
        # the loop goes until
        while len(fractional_part_bin) < (
            ieee_format.max_normalised_exp_int + 1
        ):
            print(len(fractional_part_bin))
            ic(
                fractional_part_bin,
                ieee_format.max_normalised_exp_int,
                numerator_bin,
                temp_remainder,
            )

            for bit in numerator_bin:
                temp_remainder += bit

                ic(temp_remainder)

                if len(temp_remainder) > len(remainder_after_whole_part) or len(temp_remainder) == len(remaninder_after_whole_part) and temp_remainder >= remainder_after_whole_part:
                    fractional_part_bin += "1"
                    ic(fractional_part_bin)
                    temp_remainder, remainder_after_whole_part = (
                        BinaryOperations.left_zero_pad_shorter_bin(
                            temp_remainder, remainder_after_whole_part
                        )
                    )
                    ic(temp_remainder, remainder_after_whole_part)
                    temp_remainder = BinaryOperations.subtract_binaries(
                        temp_remainder, remainder_after_whole_part
                    )
                    ic(temp_remainder, remainder_after_whole_part)
                else:
                    fractional_part_bin += "0"
        print(len(fractional_part_bin))
        # fractional_part_bin = "".join(fractional_part_bin)
        # rounding part
        if fractional_part_bin[-1] == "1":
            if fractional_part_bin[-2] == "0":
                fractional_part_bin = fractional_part_bin[:-2]
                fractional_part_bin += "1"
                is_rounded = True
            else:
                fractional_part_bin = fractional_part_bin[:-1]
        else:
            fractional_part_bin = fractional_part_bin[:-1]

        return fractional_part_bin, is_rounded
"""

    @staticmethod
    def normalise_binary_fraction(
        fractional_part_bin: str, ieee_format: IEEEFormat
    ):
        """"""
        was_normalised = False
        if fractional_part_bin[0] == "1":
            return fractional_part_bin, was_normalised

        else:
            split_parts = fractional_part_bin.split("1", 1)[0]
            left_shift = len(split_parts[0])
            fractional_part_bin = split_parts[1]
            fractional_part_bin = BinaryOperations.right_zero_pad(
                fractional_part_bin, ieee_format
            )
            was_normalised = True
            return fractional_part_bin, left_shift, was_normalised
        """
    @staticmethod
    def convert_from_binary_fraction_to_IEEE_float():
        pass

    @staticmethod
    def convert_from_IEEE_to_binary_fraction():
        pass

    @staticmethod
    def convert_from_binary_fraction_to_denary():
        pass
    """
