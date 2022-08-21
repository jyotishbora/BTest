# Runtime PoC

> Objective: implement a runtime engine that implements semantics used by legacy engine.

## Semantics

Unlike existing legacy code, the new code is pure python, but inherits the same schematics:

- Forms are defined as `Form` classes with attributes and fields
- `Calculations` are implemented as unbound functions
- `Calculations` reference arbitrary fields
- `Calculations` perform math and ternary operations

## Implementation

Classes are defined similarly to forms - class with fields with attributes:

```python
class Dog(BaseBoss):

    legs = Field(type=int, default=4, max_legs=5)
    voice = Field(loud=True, woof=True, can_be_meyauu=False)
    fir = Field(location="Everywhere", can_be_bald="of course")
```

Calculations are unbound functions:

```python
def add_legs():
    return Cat.legs + Dog.legs
```

Initiation is native:

```python
Cat = Cat(name="Koko", age=12, legs=3)
```

Math is then executed in the hydrated context (in this sample: single file with functions):

```python
    for m in [x[0] for x in inspect.getmembers(custom_math)
                    if not x[0].startswith("__")
                    and not inspect.isclass(x[1])]:
        output = getattr(custom_math, m)
        print(m, output())
```

## Construct

There are two main elements required to make it possible to call objects with original semantics:
objects called directly return a particular value and not the whole class:

```python
class BaseBoss:

    def __init__(self, *args, **kwargs):
        for kv in kwargs:
            if kv in self.get_components(Field):
                setattr(getattr(self, kv), "value", kwargs[kv])
```
In the code above, the original `Cat` class remains its attributes and properties during hydration
and also gets the `value` passed at initiation to its `value` property.

Now, that all initialized fields have values, python allows overriding ternary and math operations
that are called against objects that aren't directly calculable:

```python
    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    # ...

    def __add__(self, other):
        return self.value + other.value
```

## Running it:

`python3 runme.py` will automatically initialize two animals and run all functions from `calculations.py`

## Conclusion

Maintaining original semantics to maintain high compatibility (and comfort) is possible without
overstepping the reasonable boundaries of the language and its best practices. Due to some limitations
in python's translator, the functions and the objects cannot live in the same files (as they 
reference arbitrary objects and can cause cyclic invocation of imports) - so packaging the functions
into separate from classes packages is required - this is an inexpensive procedure.


However, updating objects referencing patterns to be more language-native to ensure some of the 
most complex operations can be performed with ease may be preferable. 

### Not implemented in this sample

- Referencing arbitrary attributes by name of the field
- More complex algebra (sqr, log etc)