# binary_number_schema.py

from marshmallow import Schema, fields


class BinaryNumberSchema(Schema):
    binary_whole_part = fields.Str(required=True)
    binary_fraction = fields.Str(required=True)
    is_positive = fields.Bool(required=True)
    sign_bit = fields.Str(required=True)


class BinaryNumberResponseSchema(Schema):
    binary_whole_part = fields.Str(required=True)
    binary_fraction = fields.Str(required=False, allow_none=True)
    is_positive = fields.Bool(required=True)
    sign_bit = fields.Str(required=True)
