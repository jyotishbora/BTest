import re
import logging
import sys
import os
import collections


logging.basicConfig(level=logging.INFO)


class MMFParser:
    types_to_ignore = ['Label', 'Line', 'Shape', 'ComboBox']
    attrs_to_ignore = ['Height', 'Width', 'Top', 'Left',
                       'Alignment', 'BackgroundColor', 'FontColor',
                       'Font', 'BoxOutline', 'LineColor']

    def __init__(self, filename):
        self.data = open(filename, 'r').read()
        self.form = self.data[self.data.index("Begin MM.Form") + len("Begin MM.Form"):self.data.index("EndForm")]
        self.form_name = re.match(r"^(.+?)\n", self.form).groups(0)[0].strip()
        self.form_attributes = dict()
        self.form_properties = dict()
        self.form_components = dict()
        self.mm_components = self.extract_mm_components(self.form, 1)
        self.form_components = self.extract_components(self.mm_components, 1)
        self.form_attributes.update(self.extract_attrs(self.form, 1))
        self.form_properties = self.extract_properties(self.form, 1)

    @property
    def required_components(self):
        return filter(
            lambda x: x['__type__'] not in self.types_to_ignore,
            self.form_components
        )

    @staticmethod
    def extract_attrs(data, padding):
        outcome = dict()
        pattern = re.compile(f"^\t{{{padding}}}(?!{'|'.join(MMFParser.attrs_to_ignore)})(\w+).*?=(.+)$")
        data = data.split("\n")
        for line in data:
            logging.debug(f"found line {line}")
            match = re.match(pattern, line)
            if match:
                logging.debug(f"line '{line}' matches attribute pattern with padding {padding}")
                groups = match.groups()
                key = groups[0].strip()
                val = groups[1].strip()
                if val.isnumeric():
                    val = int(val)
                if val in ['True', 'False']:
                    val = bool(val)
                outcome.update({key: val})
        return outcome

    @staticmethod
    def extract_properties(data, padding):
        outcome = list()
        pattern = re.compile(f"\n\t{{{padding}}}BeginProperty([\w\W]+?)\t{{{padding}}}EndProperty")
        props = re.findall(pattern, data)
        for p in props:
            """
            First line is the property name
            Properties may have multiple lines
            """
            property_dict = dict()
            property_dict.update({"__prop__": p.split("\n")[0].strip()})
            for line in p.split('\n')[1:]:
                prop_pair = line.replace("\t", "").strip().split("=")
                logging.debug(f"extracted {prop_pair}")
                if len(prop_pair) == 2:
                    val = prop_pair[1].strip()
                    if val.isnumeric():
                        val = int(val)
                    if val in ['True', 'False']:
                        val = bool(val)
                    property_dict.update({prop_pair[0].strip(): val})
                if len(prop_pair) > 2:
                    logging.error(f"got property pair with > 2 elements in property {p}")
            outcome.append(property_dict)
        return outcome

    @staticmethod
    def extract_mm_components(data, padding):
        pattern = re.compile(f"\n\t{{{padding}}}Begin MM.([\w\W]+?)\t{{{padding}}}End\n")
        return re.findall(pattern, data)

    @staticmethod
    def extract_components(data, padding):
        logging.info(f"extracted {len(data)} components")
        outcome = list()
        for item in data:
            props = MMFParser.extract_properties(item, padding + 1)
            attrs = MMFParser.extract_attrs(item, padding + 1)
            joined_props = dict()
            joined_props.update(attrs)
            for p in props:
                if len(p) == 2:
                    joined_props.update(p)
                else:
                    _name = p.get("__prop__")
                    p.pop("__prop__")
                    joined_props.update({_name: p})
            logging.debug(f"extracted {len(props)} props and {len(attrs)} attrs")
            header = item.split("\n")[0].replace("\t", "").split(" ")
            joined_props.update({'__name__': header[1], '__type__': header[0]})
            for i in joined_props:
                if isinstance(joined_props[i], str) and joined_props[i].startswith('"'):
                    new_val = joined_props[i].replace('"', "'")
                    joined_props.update({i: f'"{new_val[1:-1]}"'})
                if isinstance(joined_props[i], str) \
                        and not joined_props[i].startswith('"') \
                        and i not in ['__name__', '__type__']\
                        and not joined_props[i].isnumeric()\
                        and not joined_props[i] in ['False', 'True']:
                    joined_props.update({i: f'"{joined_props[i]}"'})
            outcome.append(joined_props)
        return outcome


def props_to_list(data: dict, remove_private=True):
    if remove_private:
        for i in ['__name__', '__type__']:
            data.pop(i, None)
    return ", ".join([f"{x}={data[x]}" for x in data if x != '__prop__'])


def parse_mmfs(filename, target_path):
    """
    Factory function to MMFParser

    """
    logging.info(f"*** Processing {filename}")
    parser = MMFParser(filename)
    logging.info(parser.form_name)

    """
    There are some properties and attributes that are either referring ENUM values or methods:
    at the time of parsing we don't know for sure (but can do some guessing)

    At this point, just to make things syntax-compliant, we're going to fix it - convert to proper string literals
    """

    for attr in parser.form_attributes:
        val = parser.form_attributes[attr]
        if isinstance(val, str) and not val.startswith('"'):
            parser.form_attributes[attr] = f'"{val}"'

    for prop in parser.form_properties:
        for key in prop:
            if isinstance(prop[key], str) and not prop[key].startswith('"') and key != '__prop__':
                prop.update({key: f'"{prop[key]}"'})

    target_file = os.path.join(target_path, f"{parser.form_name}.py")
    with open(target_file, "w") as file:
        __tab = "    "
        file.write("# This file is autogenerated, please do not edit directly!\n")
        file.write(f"from forms.Base import Form\n")
        file.write("from forms.Base import FieldSet, Property\n")
        file.write("from forms.Base import Label, TextBox, Font, CheckBox\n")
        file.write("\n\n")
        file.write(f"class {parser.form_name}(Form):\n")
        file.write(f"{__tab}# Form attributes\n")
        for attr in parser.form_attributes:
            file.writelines(f"{__tab}{attr} = {parser.form_attributes[attr]}\n")

        file.write("\n    # Form Properties\n")
        for prop in parser.form_properties:
            prop_list = [f"{x}={prop[x]}" for x in prop if x != '__prop__']
            file.write(f"{__tab}{prop.get('__prop__')} = Property({', '.join(prop_list)})\n")

        file.write("\n    # Form Components\n")

        all_name = [x.get('__name__') for x in parser.form_components]
        dupes = [key for key, count in collections.Counter(all_name).items() if count > 1]
        if dupes:
            logging.warning(f"Form {parser.form_name} has {len(dupes)} duplicate component names: {dupes}")
        collected_dupes = collections.defaultdict(list)
        for comp in parser.required_components:
            if comp.get('__name__') in dupes:
                collected_dupes[comp.get('__name__')].append(comp)
                continue
            subs = list()
            for c in comp:
                if isinstance(comp[c], dict):
                    subs.append(f"{c}={c}({props_to_list(comp[c])})")
            file.write(f"{__tab}{comp.get('__name__')} = {comp.get('__type__')}({props_to_list(comp)})\n")

        for name, dupes in collected_dupes.items():
            fields = []
            for comp in sorted(dupes, key=lambda x: int(x['Index'].strip('"'))):
                fields += [f"{comp.get('__type__')}({props_to_list(comp)})"]
            field_set = f"{name} = FieldSet(fields=[{','.join(fields)}], name={name})"
            file.write(f"{__tab}{field_set}\n")
        target_init = os.path.join(target_path, '__init__.py')
        with open(target_init, "a") as init_file:
            init_file.write(f"from .form_{parser.form_name} import {parser.form_name}\n")


if __name__ == "__main__":
    import os
    os.remove('./out/__init__.py')
    for f in os.listdir('./mmf/'):
        parse_mmfs(f)


