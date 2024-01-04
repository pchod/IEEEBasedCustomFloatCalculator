# ieee_format.py


class IEEEFormat:
    """Class representing the custom format for the IEEE binary conversion"""

    SIGN_BIT_LENGTH = 1

    def __init__(self, exponent_length: int, mantissa_length: int):
        self.exponent_length = exponent_length
        self.mantissa_length = mantissa_length
        self.bias = 2 ** (exponent_length - 1) - 1


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


class IEEE128BitFormat(IEEEFormat):
    """Class representing 128 bit float representation IEEE 754 (quadruple precision), binary128"""

    def __init__(self):
        super().__init__(exponent_length=17, mantissa_length=110)


class IEEECustomLengthFormat(IEEEFormat):
    """Class representing a custom bit-length float representation based on IEEE 754"""

    def __init__(self, exponent_length, mantissa_length):
        super().__init__(exponent_length, mantissa_length)
