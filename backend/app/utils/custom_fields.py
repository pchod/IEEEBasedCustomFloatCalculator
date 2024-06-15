import bleach
from marshmallow import fields


class SanitizedString(fields.String):
    def _deserialize(self, value, attr, data, **kwargs):
        value = super()._deserialize(value, attr, data, **kwargs)
        return bleach.clean(value)