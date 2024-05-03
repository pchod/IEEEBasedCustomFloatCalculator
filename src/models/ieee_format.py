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
        self.max_exp_value = self.BASE ** self.exponent_length - 1

        # all 1s reserved for special cases
        self.max_normalised_exp = "1" * (exponent_length - 1) + "0"
        # all 0s reserved for special cases
        self.min_normalised_exp = "0" * (exponent_length - 1) + "1"
        self.unbiased_exp_denary_value, self.max_normalised_exp_int = self._convert_exp_to_int(
            self.max_normalised_exp
        )
        self.minimal_denary_normalised = self.BASE ** self.minimum_exp_value * self.MINIMAL_NORMALISED_MANTISSA
        self.max_left_shifts, self.max_right_shifts = (
            self._calculate_possible_shifts()
        )

    def _calculate_possible_shifts(self):
        """ """
        max_left_shifts = self.BASE ** self.exponent_length - 1 - self.bias
        max_right_shifts = -self.bias

        return max_left_shifts, max_right_shifts

    def _convert_exp_to_int(self, binary: str):
        """Converting binary exponent to integer. Returns unbiased and biased exp in denary."""
        unbiased_exp_denary_value = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                unbiased_exp_denary_value += self.BASE**i

        biased_exp_denary_value = unbiased_exp_denary_value + self.bias

        return unbiased_exp_denary_value, biased_exp_denary_value




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
            (1 <= self.exponent_length <= 62)
            and (1 <= self.mantissa_length <= 62)
            and (3 <= self.total_bit_length <= 64)
        ), (
            "For the custom calculator mode: the exponent and mantissa"
            " bit-length has to be in the range from 1 to 63 and their sum"
            " cannot exceed 64 in total"
        )
