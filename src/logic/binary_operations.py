# binary_operations.py

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
    def convert_fractional_part_to_binary(num):
        bin_temp = []
        while num != 0:
            remainder = num % 2
            bin_temp.append(str(remainder))
            num = num // 2

        bin_temp.reverse()
        bin_num = "".join(bin_temp) if bin_temp else "0"
        return bin_num

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
            binary_1 = left_padding + binary_1
            return binary_1, binary_2
        else:
            left_padding = "0" * (len(binary_2) - len(binary_1))
            binary_2 = left_padding + binary_2
            return binary_1, binary_2

    @staticmethod
    def subtract_binaries(binary_1: str, binary_2: str):
        """Subtracting binary_1 - binary_2 using bitwise operations"""
        subtraction_product = []
        borrow = False

        # performing subtraction from right to left
        for index in range((len(binary_1) - 1), -1, -1):
            bit_binary_1 = binary_1[index]
            bit_binary_2 = binary_2[index]
            if borrow:
                # the borrowed bit is nullified succesfuly and borrow flag is set to false
                if bit_binary_1 == "1":
                    bit_binary_1 = "0"
                    borrow = False
                # keeping the borrow for the next iteration
                else:
                    bit_binary_1 = "1"

            if bit_binary_1 < bit_binary_2:
                borrow = True
                subtraction_product.append("1")

            elif bit_binary_1 > bit_binary_2:
                subtraction_product.append("1" if not borrow else "1")

            else:
                # for equal bits the product is 0, if the bit is borrowed, be become 1
                subtraction_product.append("1" if borrow else "0")

        subtraction_product = "".join(reversed(subtraction_product))
        return subtraction_product

    @staticmethod
    def convert_to_binary_fraction(
        denominator_bin: str, numerator_bin: str, ieee_format: IEEEFormat
    ):
        numerator_bin = numerator_bin.lstrip("0")
        denominator_bin = denominator_bin.lstrip("0")
        fraction_bin = ""
        whole_part_bin = ""
        fractional_part_bin = ""
        dividend_zero_padding = ""
        # if len(numerator_bin) <= len(denominator_bin):
        #    dividend_zero_padding = "0" * (len(denominator_bin) - len(numerator_bin))
        # numerator_bin = dividend_zero_padding + numerator_bin

        # whole part division
        remainder = ""
        divisible_num_part = ""
        for bit in numerator_bin:
            divisible_num_part += bit
            if divisible_num_part >= denominator_bin:
                whole_part_bin += "1"
                divisible_num_part = subtract_binary(
                    divisible_num_part, denominator_bin
                )

    @staticmethod
    def convert_fractional_to_binary_fraction(
        numerator: int, denominator: int, ieee_format: IEEEFormat
    ):
        pass

    @staticmethod
    def convert_decimal_to_binary_fraction():
        pass

    @staticmethod
    def normalise_binary_fraction():
        pass

    @staticmethod
    def convert_from_binary_fraction_to_IEEE_float():
        pass

    @staticmethod
    def convert_from_IEEE_to_binary_fraction():
        pass

    @staticmethod
    def convert_from_binary_fraction_to_denary():
        pass
