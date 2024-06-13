# binary_number_schema.py

from marshmallow import Schema, fields


class BinaryNumberSchema(Schema):
    binary_whole_part = fields.String(required=True)
    binary_fraction = fields.String(required=True)
    is_positive = fields.Boolean(required=True)
    sign_bit = fields.String(required=True)


class BinaryNumberResponseSchema(Schema):
    binary_whole_part = fields.String(required=True)
    binary_fraction = fields.String(required=False, allow_none=True)
    is_positive = fields.Boolean(required=True)
    sign_bit = fields.String(required=True)
