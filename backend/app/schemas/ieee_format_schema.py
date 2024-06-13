# ieee_format_schema.py

from marshmallow import Schema, fields

# ieee_format.py


class IEEEFormat:
    """Class representing the custom format for the IEEE binary conversion"""

    BASE = 2
    SIGN_BIT_LENGTH = 1
    # to represent leading 1 in the normalised form
    MINIMAL_NORMALISED_MANTISSA = 1
    def __init__(self, exponent_length: int, mantissa_length: int):
        self.exponent_length = exponent_length
        self.mantissa_length = mantissa_length
        self.bias = self.BASE ** (exponent_length - 1) - 1
        self.total_bit_length = (
            self.SIGN_BIT_LENGTH + self.exponent_length + self.mantissa_length
        )
        # in denary
        self.minimum_exp_value = -self.bias + 1
        self.maximum_exp_value = (self.BASE ** self.exponent_length - 1 - 1) - self.bias

        # all 1s reserved for special cases
        self.max_normalised_exp = "1" * (exponent_length - 1) + "0"
        # all 0s reserved for special cases
        self.min_normalised_exp = "0" * (exponent_length - 1) + "1"
        # with leading implicit 1 for normal-representation of mantissa
        self.max_mantissa_normalised_bin = "1" * mantissa_length
        self.max_mantissa_normalised_denary = 1.0 + self._convert_bin_fraction_to_float(
            self.max_mantissa_normalised_bin)
        self.minimal_denary_normalised = self.BASE ** self.minimum_exp_value * self.MINIMAL_NORMALISED_MANTISSA
        self.maximal_denary_normalised = self.BASE ** self.maximum_exp_value * self.max_mantissa_normalised_denary
        self.max_left_shifts, self.max_right_shifts = (
            self._calculate_possible_shifts()
        )

    def _calculate_possible_shifts(self):
        """ """
        max_left_shifts = self.BASE ** self.exponent_length - 1 - self.bias
        max_right_shifts = -self.bias

        return max_left_shifts, max_right_shifts

    def _convert_bin_to_int(self, binary: str):
        """Converting binary to integer."""
        int_from_bin = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                int_from_bin += self.BASE**i

        return int_from_bin

    def _convert_bin_fraction_to_float(self, binary_fraction: str):
        """
        Returns:

        """
        decimal_fraction_from_bin = 0.0
        for i, bit in enumerate(binary_fraction):
            if bit == "1":
                # i+1 to adjust 0-indexing to 1-indexing to properly represent powers
                decimal_fraction_from_bin += self.BASE ** -(i + 1)
        return decimal_fraction_from_bin




class IEEE16BitFormat(IEEEFormat):
    """Class representing 16 bit float representation IEEE 754 (half-precistion), binary16"""

    def __init__(self):
        super().__init__(exponent_length=5, mantissa_length=10)


class IEEE32BitFormat(IEEEFormat):
    """Class representing 32 bit float representation IEEE 754 (single precision), binary32"""

    def __init__(self):
        super().__init__(exponent_length=8, mantissa_length=23)


class IEEE64BitFormat(IEEEFormat):
    """Class representing 64 bit float representation IEEE 754 (double precision), binary64"""

    def __init__(self):
        super().__init__(exponent_length=11, mantissa_length=52)


class IEEECustomLengthFormat(IEEEFormat):
    """Class representing a custom bit-length float representation based on IEEE 754.
    It has to be at least 3"""

    def __init__(self, exponent_length: int, mantissa_length: int):
        super().__init__(exponent_length, mantissa_length)
        assert (
            (2 <= self.exponent_length <= 62)
            and (1 <= self.mantissa_length <= 61)
            and (4 <= self.total_bit_length <= 64)
        ), (
            "For the custom calculator mode: the exponent and mantissa"
            " bit-length has to be in the range from 1 to 63 and their sum"
            " cannot exceed 64 in total."
            " minimal exponent length is 3 and maximum mantissa length is 61."
        )
