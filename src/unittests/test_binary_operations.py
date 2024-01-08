# test_binary_operations.py
import unittest

from logic.binary_operations import BinaryOperations
from models.ieee_format import IEEE16BitFormat, IEEEFormat


class TestBinaryOperations(unittest.TestCase):
    def setUp(self):
        # Common setup for tests
        self.ieee_format = IEEE16BitFormat()
        print(f"Starting {self._testMethodName}")

    def tearDown(self) -> None:
        print(f"Completed {self._testMethodName}")

    def test_check_underflow(self):
        self.assertTrue(BinaryOperations.check_underflow(0.01, 0.005))
        self.assertFalse(BinaryOperations.check_underflow(0.01, 0.02))

    def test_check_overflow(self):
        self.assertTrue(BinaryOperations.check_overflow(100, 101))
        self.assertFalse(BinaryOperations.check_overflow(100, 99))

    def test_compare_bin_lengths(self):
        self.assertEqual(
            BinaryOperations.compare_bin_lengths("1010", "110"), 1
        )
        self.assertEqual(
            BinaryOperations.compare_bin_lengths("110", "1010"), -1
        )
        self.assertEqual(BinaryOperations.compare_bin_lengths("101", "101"), 0)

    def test_left_zero_pad_shorter_bin(self):
        self.assertEqual(
            BinaryOperations.left_zero_pad_shorter_bin("110", "1010"),
            ("0110", "1010"),
        )
        self.assertEqual(
            BinaryOperations.left_zero_pad_shorter_bin("1010", "110"),
            ("1010", "0110"),
        )

    def test_right_zero_pad(self):
        self.assertEqual(
            BinaryOperations.right_zero_pad("110", self.ieee_format),
            "110" + "0" * (self.ieee_format.mantissa_length - 3),
        )

    def test_subtract_binaries(self):
        self.assertEqual(
            BinaryOperations.subtract_binaries("1010", "0101"), "0101"
        )
        self.assertEqual(
            BinaryOperations.subtract_binaries("1101", "1010"), "0011"
        )
        self.assertEqual(
            BinaryOperations.subtract_binaries("1000", "0001"), "0111"
        )

    def test_convert_to_binary_fraction_whole_part(self):
        whole_part, remainder = (
            BinaryOperations.convert_to_binary_fraction_whole_part(
                "1010", "110"
            )
        )
        self.assertEqual(whole_part, "11")
        self.assertEqual(remainder, "10")

    def test_convert_to_binary_fraction_fraction_part(self):
        fraction_part, is_rounded = (
            BinaryOperations.convert_to_binary_fraction_fraction_part(
                "101", "01", self.ieee_format
            )
        )
        self.assertIsInstance(fraction_part, str)
        self.assertIsInstance(is_rounded, bool)
        # Note: You may need to adjust this test based on the expected behavior of the method

    def test_normalise_binary_fraction(self):
        normalised_fraction, left_shift, was_normalised = (
            BinaryOperations.normalise_binary_fraction(
                "00101", self.ieee_format
            )
        )
        self.assertEqual(normalised_fraction, "101")
        self.assertEqual(left_shift, 2)
        self.assertTrue(was_normalised)

    def test_convert_from_binary_fraction_to_IEEE_float(self):
        # Add tests for this method, once implemented
        pass

    def test_convert_from_IEEE_to_binary_fraction(self):
        # Add tests for this method, once implemented
        pass

    def test_convert_from_binary_fraction_to_denary(self):
        # Add tests for this method, once implemented
        pass


if __name__ == "__main__":
    unittest.main()
