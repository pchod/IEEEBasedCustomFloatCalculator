# ieee_float_schema.py

from marshmallow import Schema, fields, post_load
from backend.app.models.ieee_float import IEEEFloat


class IEEEFloatSchema(Schema):
    """IEEE 754 float representation"""
    sign_bit = fields.String(required=True)
    exponent = fields.String(required=True)
    mantissa = fields.String(required=True)
    calculated_exponent = fields.Integer(dump_only=True)
    is_precise = fields.Boolean(dump_only=True)
    rounded_by = fields.String(dump_only=True)
    is_special = fields.Boolean(dump_only=True)
    binary_to_convert = fields.String(dump_only=True)
    left_shifts_performed = fields.Integer(dump_only=True)
    right_shifts_performed = fields.Integer(dump_only=True)
    number_class = fields.String(dump_only=True)

    @post_load
    def create_ieee_float(self, data, **kwargs):
        return IEEEFloat(**data)

    def serialize(self, ieee_float):
        return self.dump(ieee_float)