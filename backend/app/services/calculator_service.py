from backend.app.models.binary_number import BinaryNumber
from backend.app.models.ieee_format import IEEEFormat
from backend.app.models.ieee_float import IEEEFloat
from backend.app.models.denary_number import FractionalNumber, DecimalNumber
from backend.app.models.number_representation import NumberRepresentation
from backend.app.services.binary_operations import BinaryOperations


class CalculatorService:

    @staticmethod
    def calculate_ieee_from_fractional(fractional_number: FractionalNumber, ieee_format: IEEEFormat):
        print(f"Received fractional_number: {fractional_number}")
        print(f"Using ieee_format: {ieee_format}")

        # Initialize necessary instances
        binary_number = BinaryNumber(is_positive=fractional_number.is_positive)
        ieee_float = IEEEFloat(is_positive=fractional_number.is_positive)
        number_representation = NumberRepresentation(
            fractional_number=fractional_number,
            ieee_format=ieee_format,
            ieee_float=ieee_float,
            binary_number=binary_number
        )

        # Perform calculations
        try:
            CalculatorService._calculate_and_update_binary_whole_and_fractional(number_representation)
            print(f"Binary representation: {number_representation.binary_number}")
            CalculatorService._is_precise_update(number_representation)
            normalized_fractional_part_bin, left_shifts, right_shifts = CalculatorService._get_intermediary_mantissa_and_shifts(
                number_representation)
            normalized_fractional_part_bin = CalculatorService._remove_leading_1_from_intermediary_mantissa(
                normalized_fractional_part_bin)

            # Ensure normalized_fractional_part_bin has enough length
            normalized_fractional_part_bin = CalculatorService._pad_normalized_fraction(normalized_fractional_part_bin,
                                                                                        ieee_format.mantissa_length)

            CalculatorService._calculate_and_update_calc_exp(number_representation, left_shifts, right_shifts)

            need_to_round = CalculatorService._check_if_rounding_is_needed(number_representation,
                                                                           normalized_fractional_part_bin)
            if need_to_round:
                normalized_fractional_part_bin = CalculatorService._rounding_mantissa(number_representation,
                                                                                      normalized_fractional_part_bin)

            CalculatorService._calculate_and_update_full_ieee_float(number_representation,
                                                                    normalized_fractional_part_bin)
            CalculatorService._pad_mantissa(number_representation)
            print(f"Final IEEE float representation: {number_representation.ieee_float}")

            return number_representation
        except Exception as e:
            print(f"Error during calculation: {e}")
            raise e

    @staticmethod
    def _calculate_and_update_binary_whole_and_fractional(number_representation):
        fractional_number = number_representation.denary  # Use denary
        ieee_format = number_representation.ieee_format
        numerator_bin = BinaryOperations.convert_int_to_binary(fractional_number.numerator)
        denominator_bin = BinaryOperations.convert_int_to_binary(fractional_number.denominator)
        print(f"numerator_bin: {numerator_bin}, denominator_bin: {denominator_bin}")

        whole_part_bin, remainder_bin = BinaryOperations.convert_to_binary_fraction_whole_part(numerator_bin,
                                                                                               denominator_bin)
        print(f"whole_part_bin: {whole_part_bin}, remainder_bin: {remainder_bin}")

        is_whole_part_zero = BinaryOperations.is_whole_part_zero(whole_part_bin)
        print(
            f"remainder_after_whole_part: {remainder_bin}, denominator_bin: {denominator_bin}, is_whole_part_zero: {is_whole_part_zero}, ieee_format.mantissa_length: {ieee_format.mantissa_length}")

        fractional_part_bin, is_precise = BinaryOperations.convert_to_binary_fraction_fraction_part(
            remainder_bin, denominator_bin, is_whole_part_zero, ieee_format
        )
        print(f"fractional_part_bin: {fractional_part_bin}, is_precise: {is_precise}")

        binary_number = BinaryNumber(
            binary_whole_part=whole_part_bin,
            binary_fraction=fractional_part_bin,
            is_positive=fractional_number.is_positive
        )
        number_representation.binary_number = binary_number

    @staticmethod
    def _get_intermediary_mantissa_and_shifts(number_representation):
        binary_number = number_representation.binary_number
        ieee_format = number_representation.ieee_format
        normalized_fractional_part_bin, left_shifts, right_shifts = BinaryOperations.normalise_binary_fraction(
            binary_number.binary_whole_part, binary_number.binary_fraction
        )
        print(
            f"normalized_fractional_part_bin: {normalized_fractional_part_bin}, left_shifts: {left_shifts}, right_shifts: {right_shifts}")
        return normalized_fractional_part_bin, left_shifts, right_shifts

    @staticmethod
    def _remove_leading_1_from_intermediary_mantissa(normalized_fractional_part_bin):
        print(
            f"debug: normalized fractional part {len(normalized_fractional_part_bin)} first digits before removing leading 1 {normalized_fractional_part_bin[:2]}")
        if len(normalized_fractional_part_bin) > 0 and normalized_fractional_part_bin[0] == '1':
            return normalized_fractional_part_bin[1:]
        return normalized_fractional_part_bin

    @staticmethod
    def _pad_normalized_fraction(normalized_fractional_part_bin, mantissa_length):
        # Ensure the normalized fractional part has enough length for further processing
        if len(normalized_fractional_part_bin) < mantissa_length:
            normalized_fractional_part_bin += '0' * (mantissa_length - len(normalized_fractional_part_bin))
        print(f"Padded normalized_fractional_part_bin: {normalized_fractional_part_bin}")
        return normalized_fractional_part_bin

    @staticmethod
    def _calculate_and_update_calc_exp(number_representation, left_shifts, right_shifts):
        ieee_format = number_representation.ieee_format
        calculated_exponent = BinaryOperations.calculate_normalized_exponent_int(left_shifts, right_shifts, ieee_format)
        number_representation.ieee_float.calculated_exponent = calculated_exponent
        print(f"calculated_exponent: {calculated_exponent}")

    @staticmethod
    def _check_if_rounding_is_needed(number_representation, normalized_fractional_part_bin):
        ieee_format = number_representation.ieee_format
        need_to_round = BinaryOperations.need_to_round(normalized_fractional_part_bin, ieee_format,
                                                       number_representation.denary.den_is_power_of_2)
        print(f"need_to_round: {need_to_round}")
        return need_to_round

    @staticmethod
    def _rounding_mantissa(number_representation, normalized_fractional_part_bin):
        ieee_format = number_representation.ieee_format
        rounded_fraction_bin = BinaryOperations.round_the_normalized_fractional_part(
            normalized_fractional_part_bin, ieee_format, number_representation.denary.den_is_power_of_2)
        print(f"rounded_fraction_bin: {rounded_fraction_bin}")
        return rounded_fraction_bin

    @staticmethod
    def _calculate_and_update_full_ieee_float(number_representation, normalized_fractional_part_bin):
        ieee_float = number_representation.ieee_float
        ieee_format = number_representation.ieee_format
        sign_bit, exponent, mantissa = BinaryOperations.calculate_IEEE_float(
            ieee_float.is_positive, ieee_float.calculated_exponent, normalized_fractional_part_bin, ieee_format)
        ieee_float.sign_bit = sign_bit
        ieee_float.exponent = exponent
        ieee_float.mantissa = mantissa
        print(f"sign_bit: {sign_bit}, exponent: {exponent}, mantissa: {mantissa}")

    @staticmethod
    def _is_precise_update(number_representation):
        binary_number = number_representation.binary_number
        ieee_float = number_representation.ieee_float
        ieee_float.is_precise = number_representation.denary.den_is_power_of_2
        print(f"is_precise: {ieee_float.is_precise}")

    @staticmethod
    def _pad_mantissa(number_representation: NumberRepresentation):
        if len(number_representation.ieee_float.mantissa) < number_representation.ieee_format.mantissa_length:
            number_representation.ieee_float.mantissa = number_representation.ieee_float.mantissa + '0' * (
                    number_representation.ieee_format.mantissa_length - len(
                number_representation.ieee_float.mantissa))
        print(
            f"Before padding: {number_representation.ieee_float.mantissa} (length {len(number_representation.ieee_float.mantissa)})")
