from runtime.sample_two import base


class Cat(base.BaseBoss):

    name = base.Field(name="Unknown", changes=False, understandable=True)
    age = base.Field(type=int, max_age=256)
    legs = base.Field(type=int, default=4, can_be_0=True)




