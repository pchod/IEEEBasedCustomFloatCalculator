# ieee_format_schema.py

from marshmallow import Schema, fields, post_load, validates_schema, ValidationError
from backend.app.models.ieee_format import (IEEEFormat, IEEE16BitFormat, IEEE32BitFormat, IEEE64BitFormat,
                                            IEEECustomLengthFormat)


class IEEEFormatSchema(Schema):
    exponent_length = fields.Int(required=True)
    mantissa_length = fields.Int(required=True)
    bias = fields.Int(dump_only=True)
    total_bit_length = fields.Int(dump_only=True)
    minimum_exp_value = fields.Int(dump_only=True)
    maximum_exp_value = fields.Int(dump_only=True)
    max_normalised_exp = fields.Str(dump_only=True)
    min_normalised_exp = fields.Str(dump_only=True)
    max_mantissa_normalised_bin = fields.Str(dump_only=True)
    max_mantissa_normalised_denary = fields.Float(dump_only=True)
    minimal_denary_normalised = fields.Float(dump_only=True)
    maximal_denary_normalised = fields.Float(dump_only=True)
    max_left_shifts = fields.Int(dump_only=True)
    max_right_shifts = fields.Int(dump_only=True)

    @post_load
    def make_ieee_format(self, data, **kwargs):
        return IEEEFormat(**data)


class IEEE16BitFormatSchema(IEEEFormatSchema):
    @post_load
    def make_ieee_format(self, data, **kwargs):
        return IEEE16BitFormat()


class IEEE32BitFormatSchema(IEEEFormatSchema):
    @post_load
    def make_ieee_format(self, data, **kwargs):
        return IEEE32BitFormat()


class IEEE64BitFormatSchema(IEEEFormatSchema):
    @post_load
    def make_ieee_format(self, data, **kwargs):
        return IEEE64BitFormat()


class IEEECustomLengthFormatSchema(IEEEFormatSchema):
    @post_load
    def make_ieee_format(self, data):
        return IEEECustomLengthFormat(**data)
