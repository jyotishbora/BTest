

def get_string(value):
    return str(value)


def get_currency(value):
    return float(value)


def get_bool(value):
    return bool(value)


def get_number(value):
    return int(value)


def trim(value):
    return str(value).strip()


def max_value(*values):
    mv = -1000000000000000
    for v in values:
        if v > mv:
            mv = v
    return mv


def min_value(*values):
    mv = 10**8
    for v in values:
        if v < mv:
            mv = v
    return mv


def get_float(value):
    return float(value)


def c_dollar(value):
    return round(float(value))
