# transforms original and python files into one-liners
import os
import re


def transform_bas(file) -> str:
    lines = list()
    data = open(file, 'r').read()
    pattern = re.compile("(Sub .+?\([\w\W]*?End Sub)")
    for m in re.findall(pattern, data):
        m = m.replace("    ", "\t")
        m = m.replace("\t", "{t}")
        m = m.replace("\n", "{n}")
        lines.append(m)
    return lines


def transform_py(file) -> str:
    lines = list()
    data = open(file, 'r').read()
    # todo: this regex catches one creepy string with "def" in it
    pattern = re.compile("(def*\W\w+[\w\W]*?)(?=(def)|$)")
    for m in re.findall(pattern, data):
        mm = m[0].replace("    ", "\t")
        mm = mm.replace("\t", "{t}")
        mm = mm.replace("\n", "{n}")
        lines.append(mm)
    return lines


if __name__ == "__main__":
    with open("data/input_bas.txt", "w") as file:
        files = os.listdir("../forms/calc/bas/")
        files.sort()
        for bas_file in files:
            result = transform_bas(f"../forms/calc/bas/{bas_file}")
            file.write("\n".join(result))

    with open("data/input_py.txt", "w") as file:
        files = os.listdir("../forms/calc/py-processed/")
        files.sort()
        for py_file in files:
            result = transform_py(f"../forms/calc/py-processed/{py_file}")
            file.write("\n".join(result))
