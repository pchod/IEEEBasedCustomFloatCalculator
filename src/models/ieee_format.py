# ieee_format.py


class IEEEFormat:
    """Class representing the custom format for the IEEE binary conversion"""

    BASE = 2
    SIGN_BIT_LENGTH = 1

    def __init__(self, exponent_length: int, mantissa_length: int):
        self.exponent_length = exponent_length
        self.mantissa_length = mantissa_length
        self.bias = 2 ** (exponent_length - 1) - 1
        self.total_bit_length = (
            self.SIGN_BIT_LENGTH + self.exponent_length + self.mantissa_length
        )
        self.minimum_exp = -(self.bias) + 1
        self.max_normalised_exp = "1" * (exponent_length - 1) + "0"
        _, self.max_normalised_exp_int = IEEEFormat.convert_exp_to_int(
            self.max_normalised_exp
        )

    @staticmethod
    def convert_exp_to_int(binary: str):
        """Converting exponent to integer"""
        unbiased_exp_denary = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                unbiased_exp_denary += IEEEFormat.BASE**i

        biased_exp_denary = unbiased_exp_denary + IEEEFormat.bias

        return unbiased_exp_denary, biased_exp_denary


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
        super().__init__(exponent_length=13, mantissa_length=50)


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
