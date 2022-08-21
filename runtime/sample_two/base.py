import inspect


class BaseBoss:

    def __init__(self, *args, **kwargs):
        for kv in kwargs:
            if kv in self.get_components(Field):
                setattr(getattr(self, kv), "value", kwargs[kv])

    def get_components(self, t: type) -> list:
        outcome = list()
        for i in inspect.getmembers(self):
            if isinstance(i[1], t):
                outcome.append(i[0])
        return outcome


class Field:

    def __init__(self, *args, **kwargs):
        for kv in kwargs:
            setattr(self, kv, kwargs[kv])

    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __ge__(self, other):
        return self.value >= other

    def __le__(self, other):
        return self.value <= other

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __floordiv__(self, other):
        return round(self.value / other.value)

    def __truediv__(self, other):
        return self.value / other.value
    


