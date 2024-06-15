def is_valid_base10_int(value):
    try:
        int(value, 10)
        return True
    except ValueError:
        return False


def is_valid_base10_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
