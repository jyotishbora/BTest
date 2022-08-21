from runtime.sample_two import base
from dog import Dog


class Cat(base.BaseBoss):

    name = base.Field(name="Kitty", changes=False, understandable=True)
    age = base.Field(type=int, max_age=256)
    legs = base.Field(type=int, default=4, can_be_0=True)


def compare_to_dog():
    if Dog.legs > Cat.legs:
        return "cat wins"
