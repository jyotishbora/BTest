from cat import Cat
from dog import Dog


def compare_to_dog():
    if Dog.legs > Cat.legs:
        return "cats win anyway"


def calculate_age():
    if Cat.age > 10:
        return 5
    else:
        return 12


def add_legs():
    return Cat.legs + Dog.legs


def divide_legs():
    return Cat.legs / Dog.legs


def show_cat():
    return Cat
