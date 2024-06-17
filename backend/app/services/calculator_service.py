from backend.app.models.binary_number import BinaryNumber
from backend.app.models.ieee_format import IEEEFormat
from backend.app.models.ieee_float import IEEEFloat
from backend.app.models.denary_number import FractionalNumber, DecimalNumber
from backend.app.models.number_representation import NumberRepresentation
from backend.app.services.binary_operations import BinaryOperations
from backend.app.utils.ieee_utils import IEEEUtils


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
            number_representation.ieee_float.number_class = IEEEUtils.get_ieee_class_for_fractional(number_representation.denary.decimal_float_derived, number_representation.denary.denominator, number_representation.denary.is_positive, number_representation.ieee_format.minimal_denary_normalised, number_representation.ieee_format.maximal_denary_normalised)
            # if number_representation.ieee_format.number_class != "normal" or "subnormal":
            if number_representation.ieee_float.number_class not in {"normal", "subnormal"}:
                CalculatorService._create_special_representation_of_ieee_float(number_representation)
                return number_representation
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
    def calculate_ieee_from_decimal(decimal_number: DecimalNumber, ieee_format: IEEEFormat):
        print(f"Received decimal_number: {decimal_number}")
        print(f"Using ieee_format: {ieee_format}")

        # Initialize necessary instances
        binary_number = BinaryNumber(is_positive=decimal_number.is_positive)
        ieee_float = IEEEFloat(is_positive=decimal_number.is_positive)
        number_representation = NumberRepresentation(
            decimal_number=decimal_number,
            ieee_format=ieee_format,
            ieee_float=ieee_float,
            binary_number=binary_number
        )
        #needs review:
        try:
            CalculatorService._calculate_scientific_bin_from_decimal(number_representation)
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

            return number_representation
        except Exception as e:
            print(f"Error during calculation: {e}")
            raise e


    @staticmethod
    def _calculate_scientific_bin_from_decimal(number_representation):
        decimal_number = number_representation.denary
        ieee_format = number_representation.ieee_format
        whole_part_bin = BinaryOperations.convert_int_to_binary(decimal_number.int_part)
        numerator_bin = BinaryOperations.convert_int_to_binary(decimal_number.fractional_part)
        denominator_bin = BinaryOperations.convert_int_to_binary(decimal_number.scale_factor)
        print(f"numerator_bin: {numerator_bin}, denominator_bin: {denominator_bin}")
        is_whole_part_zero = decimal_number.is_decimal_zero
        fractional_part_bin, is_precise = BinaryOperations.convert_to_binary_fraction_fraction_part(
            numerator_bin, denominator_bin, is_whole_part_zero, ieee_format
        )
        print(f"fractional_part_bin: {fractional_part_bin}, is_precise: {is_precise}")

        binary_number = BinaryNumber(
            binary_whole_part=whole_part_bin,
            binary_fraction=fractional_part_bin,
            is_positive=decimal_number.is_positive
        )
        number_representation.binary_number = binary_number

    @staticmethod
    def _create_special_representation_of_ieee_float(number_representation: NumberRepresentation):
        ieee_float = number_representation.ieee_float
        ieee_format = number_representation.ieee_format
        if ieee_float.number_class.lower() == "nan":
            ieee_float.sign_bit, ieee_float.exponent, ieee_float.mantissa = CalculatorService._construct_nan_representation(ieee_format)
            return
        elif "infinity" in ieee_float.number_class.lower():
            ieee_float.sign_bit, ieee_float.exponent, ieee_float.mantissa = CalculatorService._construct_inf_representation(ieee_format, ieee_float.is_positive)
        elif "zero" in ieee_float.number_class.lower():
            ieee_float.sign_bit, ieee_float.exponent, ieee_float.mantissa = CalculatorService._construct_zero_representation(ieee_format, ieee_float.is_positive)

    @staticmethod
    def _construct_nan_representation(ieee_format: IEEEFormat):
        """
        The method contructs a quiet NaN representation for a given IEEE format.
        Returns:
            - sign bit set to 0;
            - exponent
        """
        sign_bit = "0"
        exponent = "1" * ieee_format.exponent_length
        mantissa = "1" + "0" * (ieee_format.mantissa_length - 1)
        return sign_bit, exponent, mantissa
    @staticmethod
    def _construct_inf_representation(ieee_format: IEEEFormat, is_positive: bool):
        """

        """
        sign_bit = "0" if is_positive else "1"
        exponent = "1" * ieee_format.exponent_length
        mantissa = "0" * ieee_format.mantissa_length
        return sign_bit, exponent, mantissa
    @staticmethod
    def _construct_zero_representation(ieee_format: IEEEFormat, is_positive: bool):
        mantissa = "0" * ieee_format.mantissa_length
        exponent = "0" * ieee_format.exponent_length
        sign_bit = "0" if is_positive else "1"
        return sign_bit, exponent, mantissa


    @staticmethod
    def _calculate_and_update_binary_whole_and_fractional(number_representation):
        fractional_number = number_representation.denary
        ieee_format = number_representation.ieee_format
        numerator_bin = BinaryOperations.convert_int_to_binary(fractional_number.numerator)
        denominator_bin = BinaryOperations.convert_int_to_binary(fractional_number.denominator)
        print(f"numerator_bin: {numerator_bin}, denominator_bin: {denominator_bin}")

        whole_part_bin, remainder_bin = BinaryOperations.new_whole_part_long_division(numerator_bin,
                                                                                               denominator_bin)
        print(f"whole_part_bin: {whole_part_bin}, remainder_bin: {remainder_bin}")

        is_whole_part_zero = BinaryOperations.is_whole_part_zero(whole_part_bin)
        print(
            f"remainder_after_whole_part: {remainder_bin}, denominator_bin: {denominator_bin}, is_whole_part_zero: {is_whole_part_zero}, ieee_format.mantissa_length: {ieee_format.mantissa_length}")
        #check for subnormal - for further improvement SUBNORMAL REPRESENTATIONS
        if not is_whole_part_zero:
            is_subnormal = BinaryOperations.is_subnormal_whole_part(whole_part_bin, ieee_format.max_right_shifts)

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
