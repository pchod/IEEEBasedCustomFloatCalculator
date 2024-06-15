# binary_number_schema.py

from marshmallow import Schema, fields, post_load, ValidationError, validates

from backend.app.models.binary_number import BinaryNumber


class BinaryNumberSchema(Schema):
    binary_whole_part = fields.String(required=True)
    binary_fraction = fields.String(required=True)
    is_positive = fields.Boolean(required=True)
    sign_bit = fields.String(dump_only=True)

    @validates('binary_whole_part')
    def validate_binary_whole_part(self, value):
        if not all(char in {'0', '1'} for char in value):
            raise ValidationError("binary_whole_part can only contain '0' or '1'.")

    @validates('binary_fraction')
    def validate_binary_fraction(self, value):
        if not all(char in {'0', '1'} for char in value):
            raise ValidationError("binary_fraction can only contain '0' or '1'.")

    @post_load
    def create_binary_number(self, data):
        return BinaryNumber(**data)

    def serialize(self, binary_number):
        return self.dump(binary_number)

