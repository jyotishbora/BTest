from runtime.sample_two.base import Field, BaseBoss


class Dog(BaseBoss):

    legs = Field(type=int, default=4, max_legs=5)
    voice = Field(loud=True, woof=True, can_be_meyauu=False)
    fir = Field(location="Everywhere", can_be_bald="of course")


