import os
import sys
import re
import logging
from .Base import Function
import networkx as nx
import matplotlib.pyplot as plt
import pickle
import subprocess
logging.basicConfig(level=logging.INFO)


class Extractor:

    def __init__(self, file):
        self.functions = list()
        self.data = open(file, "r").read()
        self.form_name = re.findall(r"Begin MM.Form (\w+?)\n", self.data)[0]
        logging.debug(f"Processing form {self.form_name}")
        # self.extract("Private Sub (.+?)(\([\w\W]*?)End Sub")
        self.extract("Sub (.+?)(\([\w\W]*?)End Sub")

    def extract(self, pattern):
        pattern = re.compile(pattern)
        matches = re.findall(pattern, self.data)
        logging.debug(f"{len(matches)} matches found")
        for m in matches:
            f = Function()
            f.form = self.form_name
            f.name = m[0]
            code = m[1].split("\n")
            f.params = code[0].strip()
            f.code = "\n".join(code[1:-1])
            self.functions.append(f)

    def save_to_file(self):
        for func in self.functions:
            with open(f"calc/{func.name}", "wb") as f:
                pickle.dump(func, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def get_all_mmf_functions(base_dir):
        outcome = list()
        for file in [x for x in os.listdir(base_dir) if x.endswith(".mmf")]:
            logging.debug(f"Processing file {file}")
            outcome = outcome + Extractor(os.path.join(base_dir, file)).functions
        return outcome

    @staticmethod
    def funcs_to_file(source, target):
        e = Extractor(source)
        with open(target, "w") as tar:
            for f in e.functions:
                tar.write(f"Private Sub {f.name}{f.params}\n{f.code}\nEnd Sub\n\n")

    @staticmethod
    def graph_all():
        all_functions = list()
        for file in os.listdir("./mmf/"):
            e = Extractor(f"./mmf/{file}")
            all_functions = all_functions + e.functions
        logging.info(f"Found {len(all_functions)} functions globally")
        g = nx.DiGraph()
        for f in all_functions:
            for x in all_functions:
                if f.form in x.code and x.form != f.form:
                    g.add_edge(x.name, f.form)
        print(f"{len(g.edges())} edges")
        # pos = nx.nx_agraph.graphviz_layout(g, prog='neato')
        pos = nx.spring_layout(g, k=0.2, iterations=100)
        plt.figure(1, (20, 20))
        nx.draw(g, with_labels=True, font_size=8, node_size=40, pos=pos, arrowsize=8, width=0.4, edge_color="grey")
        plt.savefig("./graphs/func-form-graph.pdf", dpi=10000)

    @staticmethod
    def rename_gets(f):
        with open(f, "w") as file:
            file.seek(0, 0)





if __name__ == "__main__":
    """
    Generates stats on things
    af = Extractor.get_all_functions()
    lines = [len(x.code_formatted) for x in af]
    lines.sort()
    lines.reverse()
    [print(f"{x.form}->{x.name}{x.params}: {x.code}") for x in af if len(x.code_formatted) == 1]
    [print(f"{x.name}{x.params}: {len(x.code_formatted)} lines") for x in af if x.params != "()"]
    print(lines)
    print(lines.count(1))
    """

    """
    Converts files from vb to python with vb2py module
    subprocess.run(["pwd",])
    for f in os.listdir("./mmf/"):
        Extractor.funcs_to_file(f"./mmf/{f}", f"./calc/bas/{f[:-4]}.bas")
        subprocess.run(["./convert.sh", f"/Users/aleksandr.bolotnov/Projects/Blucora/forms/calc/bas/{f[:-4]}.bas",
                        f"/Users/aleksandr.bolotnov/Projects/Blucora/forms/calc/py"])
        subprocess.run(["mv", "./calc/py/None.py", f"./calc/py/{f[:-4]}.py"])
    """


