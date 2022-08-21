import inspect
from typing import List
from dataclasses import dataclass


class FreeArgsBase:
    def __init__(self, **kwargs):
        for kv in kwargs:
            setattr(self, kv, kwargs[kv])


class Form(FreeArgsBase):

    def get_components(self, t: type) -> list:
        outcome = list()
        for i in inspect.getmembers(self):
            if isinstance(i[1], t):
                outcome.append(i[0])
        return outcome


class Field(FreeArgsBase):

    @property
    def value(self):
        return self.value


@dataclass
class FieldSet:
    name: str
    fields: List[Field]


class Font(FreeArgsBase):
    pass


class Property(FreeArgsBase):
    pass


class Label(Field):
    pass


class TextBox(Field):
    pass


class CheckBox(Field):
    pass


class Shape(FreeArgsBase):
    pass


class Line(FreeArgsBase):
    pass


class ComboBox(FreeArgsBase):
    pass


@dataclass
class Function:
    name: str = ""
    form: str = ""
    code: str = ""
    params: str = ""

    @property
    def code_formatted(self):
        return self.code.split("\n")
