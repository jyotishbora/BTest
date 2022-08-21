# MMF -> Python PoC

> Apologies for dirty code - I was trying to do this quickly

## What it does - forms conversion

`parser.py` will take all files from `mmf` directory and generate python files in `out`
and also add their imports to `__init__.py` so that it acts as a module and allows importing directly. 
I also included the `black` folder - which is a copy of the forms generated in `out` and processed with `black`
code formatter tool - it does not change anything in the code, just formats it nicely.

What the code does:

- extracts form attributes
- extracts form properties (they can be multiline, so they are wrapped into `Property` class)
- extracts all form components and their attributes/properties and wrap them into their proper classes
- rename enumerators for `Label` and `Line` since they are not unique
- convert types to pythonic where possible to do this quickly: `int`, `bool`

## What it does - math conversion

`math_exporter` does a few things - it will export all formulas into objects and save them as pickle files,
this is not really required anymore, it will also run a shell script that uses `vb2py` module to convert them to python.
The converted files go to `py` folder. This conversion is very raw and `math_processor` file will attempt 
to complete it - rename some references to global helper functions and also resolve references to the forms and import them.
Completed conversions end up in `py-processed` folder.


## What all these files mean

`forms` directory contains the following:

- `mmf` - original form master files
- `out` - processed files as python class files
- `black` - same content as in `out` but with better formatting

`forms/math` directory contains the following:

- `bas` - all functions exported from original `mmf` forms
- `py` - functions converted to python code with `vb2py` app
- `py-processed` (WIP) - all files post-processed after original `vb2py` conversion
- `tools.py` is the file that contains some "helper" functions definitions that are not in the `mmm` files

## Proof that forms convert properly?

There is a basic test in `tests.py` file that demonstrates how each individual form class is initiated:
this would only happen if the content of the class is structurally and syntactically correct. There is also a test
to make sure all classes generated successfully.

## Key problems that may require some PoC work

> There are many, I am focusing on the ones that I think are most important

### Referential integrity of the math code

`py_compile` and `ast` don't seem to do a good job figuring out reference errors, but `pyflakes` does.
However, `pyflakes` does not look behind the `*` imports:

> ./forms/math/py-processed/IAF1040.py:1173:8 'get_bool' may be undefined, or defined from star imports: forms.math.tools, vb2py.vbdebug, vb2py.vbfunctions

It does not have any configuration options to enable this (and besides, importing * is bad practice),
so while we use automatic generation of code anyway, we need to fix the imports for `vb2py` functions and
`tools` functions, too. I actually want to move `vb2py` as well and revisit some of the classes they have,
I think there are suboptimal.

### Form linked attributes are not always fields

Here is a field from one of the form files:

`Single = CheckBox(FieldName="Single", FieldType="CheckBox", FieldVersion="" VirtualArraySize="", FieldDesc="", Caption="Single:", TabSequence=17, DefaultVal="", QuickEntry=True, RadioTag="MFJ")`

There is a property `RadioTag="MFJ`

Here is a sample of code from one of the functions:

`if get_bool(IAF1040.MFJ) == True or get_bool(IAF1040.CombMFS) == True:`

Intuitively, one would think that these references are always in the format of `form.field`, but it's not 
always the case like in the example above (btw, `CombMFS` reference in `IAF1040` for is a field if the form: `CombMFS = CheckBox(FieldName="CombMFS"...)`)

### Hydrating math context

Interesting challenge. There are multiple places in the systems where functions live:

- `mmf` form files: so far I haven't seen a single file that does the `Call` routine that is typical for `mmm` files
- `mmm` files seem to be mainly combined of `Call` and some `enum` and lists definitions

Interestingly, `mmm` files can contain both `Sub()` functions and `Function()` and these functions can be 
private and public while all `Sub()` in forms appear to be private.

Any form function can reference multiple other forms to perform calculations. Functions don't instantiate 
form classes and populate their context - there seems something behind the scenes that does it for them.

### Cyclic references

One of the large problems is cyclic references that may be hard to overcome:

if you have a form `A` referencing for `B` that has functions referencing form `A` you will end up with
`A->B & B->A` and it will not work.

I think the solution here is to merge all functions into a single file and once import all forms and hydrate
them during initialization.

## Next steps

- If you look at the `draw` method - there is some basic code that renders some form elements with `Tk`:
more research is required to understand the coordinates system used in the original forms - not directly compatible
with the `Tk` layouts.
- Need to extract math - it would require constructing lex though most likely
- Need to find some components that can support managing forms with direct code output


## Further research, findings

- http://www.python-gui-builder.com - interesting little tool that generates python code for `Tk` forms on the fly
- https://visualtk.com - better visual tool that generates UI/HTML _and_ python `Tk` code
- http://vb2py.sourceforge.net/ - interesting library that does conversion from VB to Python:
it's not very easy to use and requires some dancing around it to make it work right, it does not
convert many things ideally: VB `if <condition> = True` converts into `if <condition> == True:`
instead of `if <condition>:`
but it's a good "pre-parser" potentially
- https://github.com/uwol/proleap-vb6-parser ast for vb6, java though
- https://github.com/facebookresearch/CodeGen - free pre-trained model for conversion between languages
- https://github.com/dabeaz/sly - kinda like ANTLR but easier to understand I guess

## Notes

- Many files have non-utf8 in them, utf8cleaner has command line interface
