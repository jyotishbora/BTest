import os
import re
import sys
import inspect
from forms import out
from types import ModuleType


replace_pairs = {
    'GetString': 'get_string',
    'GetBool': 'get_bool',
    'GetCurrency': 'get_currency',
    'Trim': 'trim',
    'GetNumber': 'get_number',
    'MaxValue': 'max_value',
    'GetFloat': 'get_float',
    'CDollar': 'c_dollar',
    'MinValue': 'min_value'
}


def replace_tool_func_calls(func: str):
    """
    This is not exactly correct to just replace, because this will also fuck up `Private Sub GetString()` for instance
    But will do for the PoC
    """
    for r in replace_pairs:
        func = func.replace(f"{r}(", f"{replace_pairs[r]}(")
    return func


def replace_form_references(func: str):
    forms = [x[0] for x in inspect.getmembers(out) if not x[0].startswith("__") and not isinstance(x[1], ModuleType)]
    imports = list()
    for f in forms:
        matches = re.findall(f, func, re.IGNORECASE)
        if matches:
            for m in matches:
                func = func.replace(m, f)
                imp = f"from forms.out import {f}\n"
                if imp not in imports:
                    imports.append(imp)
    tools_imp = "from forms.calc.tools import *\n"
    if tools_imp not in imports:
        imports.append(tools_imp)
    func = "".join(imports) + func + '\n'
    return func


def replace_return_value(func):
    """
    Dirty and needs proper matching with regex but will do for now
    """
    return func.replace('ReturnVal = ', 'return ')


if __name__ == '__main__':
    for file in os.listdir("calc/py/"):
        handler = open(f"calc/py/{file}", 'r')
        func = handler.read()
        func = replace_tool_func_calls(func)
        func = replace_form_references(func)
        func = replace_return_value(func)
        with open(f"calc/py-processed/{file}", "w") as target:
            target.write(func)

