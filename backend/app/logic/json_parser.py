import json


class JSONParser:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            self.json_data = json.load(file)

    def parse_path(self):
        path = self.json_data.get("path")
        return path

    def parse_ieee_format(self):
        ieee_format = self.json_data.get("ieee_format")
        exponent_length = None
        mantissa_length = None
        if ieee_format == "custom":
            exponent_length = self.json_data.get("exponent_length")
            mantissa_length = self.json_data.get("mantissa_length")
        return ieee_format, exponent_length, mantissa_length

    def parse_fractional(self):
        is_positive = self.json_data.get("is_positive")
        numerator = self.json_data.get("numerator")
        denominator = self.json_data.get("denominator")
        return is_positive, numerator, denominator

    def parse_decimal(self):
        is_positive = self.json_data.get("is_positive")
        int_part = self.json_data.get("int_part")
        fract_part = self.json_data.get("fract_part")
        return is_positive, int_part, fract_part

    def parse_ieee_representation(self):
        sign_bit = self.json_data.get("sign_bit")
        exponent_bits = self.json_data.get("exponent_bits")
        mantissa_bits = self.json_data.get("mantissa_bits")
        return sign_bit, exponent_bits, mantissa_bits
