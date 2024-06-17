# ieee_utils.py
from backend.app.models.ieee_format import IEEEFormat

class IEEEUtils():
    @staticmethod
    def get_ieee_class_for_fractional(decimal_fraction: float, denominator: int, is_positive: bool, min: float, max: float):
        if denominator == 0 or decimal_fraction != decimal_fraction:
            return IEEEFormat.CLASS_NAN
        elif min < decimal_fraction < max:
            return IEEEFormat.CLASS_NORMAL
        elif 0.0 < decimal_fraction < min:
            return IEEEFormat.CLASS_SUBNORMAL
        elif decimal_fraction == 0.0 and is_positive:
            return IEEEFormat.CLASS_ZERO_POSITIVE
        elif decimal_fraction == 0.0 and not is_positive:
            return IEEEFormat.CLASS_ZERO_NEGATIVE
        elif decimal_fraction > max and is_positive:
            return IEEEFormat.CLASS_INFINITY_POSITIVE
        elif decimal_fraction > max and not is_positive:
            return IEEEFormat.CLASS_INFINITY_NEGATIVE