import unittest

from models.ieee_format import (
    IEEE16BitFormat,
    IEEE32BitFormat,
    IEEE64BitFormat,
    IEEECustomLengthFormat,
    IEEEFormat,
)


class TestIEEEFormat(unittest.TestCase):
    def test_initialization(self):
        # Test initialization and attributes of IEEEFormat
        format = IEEEFormat(5, 10)
        self.assertEqual(format.exponent_length, 5)
        self.assertEqual(format.mantissa_length, 10)
        self.assertEqual(format.bias, 15)
        self.assertEqual(format.total_bit_length, 16)
        self.assertEqual(format.minimum_exp, 2 ** (1 - 15))
        self.assertEqual(
            format.max_normalised_exp_int,
            IEEEFormat.convert_exp_to_int(format.max_normalised_exp),
        )

    def test_convert_exp_to_int(self):
        # Test convert_exp_to_int method
        self.assertEqual(IEEEFormat.convert_exp_to_int("110"), 6)
        self.assertEqual(IEEEFormat.convert_exp_to_int("0"), 0)
        self.assertEqual(IEEEFormat.convert_exp_to_int("1"), 1)
        self.assertEqual(IEEEFormat.convert_exp_to_int("101"), 5)

    def test_subclass_initialization(self):
        # Test initialization of subclasses
        format16 = IEEE16BitFormat()
        self.assertEqual(format16.exponent_length, 5)
        self.assertEqual(format16.mantissa_length, 10)

        format32 = IEEE32BitFormat()
        self.assertEqual(format32.exponent_length, 8)
        self.assertEqual(format32.mantissa_length, 23)

        format64 = IEEE64BitFormat()
        self.assertEqual(format64.exponent_length, 13)
        self.assertEqual(format64.mantissa_length, 50)

    def test_custom_format_constraints(self):
        # Test constraints for custom format
        with self.assertRaises(AssertionError):
            IEEECustomLengthFormat(0, 64)
        with self.assertRaises(AssertionError):
            IEEECustomLengthFormat(63, 0)
        with self.assertRaises(AssertionError):
            IEEECustomLengthFormat(2, 63)

        # Valid custom format
        try:
            IEEECustomLengthFormat(3, 60)
        except AssertionError:
            self.fail(
                "IEEECustomLengthFormat raised AssertionError unexpectedly!"
            )


# Run the tests
if __name__ == "__main__":
    unittest.main()
