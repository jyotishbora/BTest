import collections
import sys
from types import ModuleType
from forms import out
import inspect
from Base import TextBox


class Analyzer:

    def __init__(self, instance):
        self.instance = instance

    @property
    def info(self):
        info = dict()
        info['FormName'] = getattr(self.instance, "FormName", None)
        info['fields_by_class'] = self.fields_by_class
        info['textboxes_by_type'] = self.textbox_by_type
        return info

    @property
    def fields_by_class(self):
        fields = dict()
        for f in inspect.getmembers(self.instance):
            ft = type(f[1]).__name__
            if ft in ['wrapper_descriptor', 'builtin_function_or_method',
                      'getset_descriptor', 'mappingproxy', 'method_descriptor', 'NoneType', 'type']:
                continue
            if ft in fields:
                fields[ft] = fields[ft]+1
            else:
                fields[ft] = 1
        return fields

    @property
    def textbox_by_type(self):
        boxes = set()
        for f in inspect.getmembers(self.instance):
            if type(f[1]).__name__ == "TextBox":
                boxes.add(getattr(f[1], 'FieldType', 'Unset'))
        return boxes


if __name__ == "__main__":
    for item in inspect.getmembers(out):
        if not item[0].startswith("__") and not isinstance(item[1], ModuleType):
            a = Analyzer(getattr(out, item[0]))
            print(a.info)

