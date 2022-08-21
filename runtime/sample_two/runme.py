from cat import Cat
from dog import Dog
from runtime.sample_two import calculations as custom_math
import inspect
from types import ModuleType


if __name__ == "__main__":

    Cat = Cat(name="Koko", age=12, legs=3)
    Dog = Dog(legs=4, voice="Brrrraaff", fir="black")

    for m in [x[0] for x in inspect.getmembers(custom_math) if not x[0].startswith("__")
                                                               and not inspect.isclass(x[1])]:
        output = getattr(custom_math, m)
        print(m, output())
