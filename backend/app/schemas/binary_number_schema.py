# binary_number_schema.py

from marshmallow import Schema, fields, post_load

from backend.app.models.binary_number import BinaryNumber


class BinaryNumberSchema(Schema):
    binary_whole_part = fields.String(required=True)
    binary_fraction = fields.String(required=True)
    is_positive = fields.Boolean(required=True)
    sign_bit = fields.String(dump_only=True)

    @post_load
    def create_binary_number(self, data):
        return BinaryNumber(**data)

    def serialize(self, binary_number):
        return self.dump(binary_number)
    
