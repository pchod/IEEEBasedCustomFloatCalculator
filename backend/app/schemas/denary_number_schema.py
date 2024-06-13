# denary_number_schema.py

from marshmallow import Schema, fields


class FractionalNumberSchema(Schema):
    numerator = fields.Integer(required=True)
    denominator = fields.Integer(required=True)
    is_positive = fields.Boolean(required=True)
    numerator_entered = fields.Integer(dump_only=True)
    denominator_entered = fields.Integer(dump_only=True)
    den_is_power_of_2 = fields.Boolean(dump_only=True)
    decimal_float_derived = fields.Float(dump_only=True)


class DecimalNumber(DenaryNumber):
    int_part = fields.String(required=True)
    fractional_part = fields.String(required=True)
    is_positive = fields.Boolean(required=True)
    decimal_number = fields.String(dump_only=True)
    is_decimal_zero = fields.Boolean(dump_only=True)
    numerator_derived = fields.Integer(dump_only=True)
    denominator_derived = fields.Integer(dump_only=True)
    den_derived_is_power_of_2 = fields.Boolean(dump_only=True)
