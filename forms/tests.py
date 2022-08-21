import re
import unittest
import inspect
from types import ModuleType
import os


class BasicTests(unittest.TestCase):

    def test_modules_init(self):
        from forms import out
        for item in inspect.getmembers(out):
            if not item[0].startswith("__") and not isinstance(item[1], ModuleType):
                _ = getattr(out, item[0])
                print(_.FormName, "initialized ok")
                self.assertGreater(len(_.FormName), 0)

    def test_all_classes_generated(self):
        from forms import out
        self.assertEqual(len(os.listdir("./mmf/")), len([x for x in inspect.getmembers(out) if
                                                         not x[0].startswith("__")
                                                         and not isinstance(x[1], ModuleType)]))

    def test_depgraph(self): # noqa typo
        import networkx as nx
        import matplotlib.pyplot as plt
        from forms import out
        G = nx.DiGraph() # noqa
        forms_files = os.listdir("./mmf/")
        form_names = [x for x in inspect.getmembers(out) if not x[0].startswith("__")
                      and not isinstance(x[1], ModuleType)]
        for f in forms_files:
            with open(f"./mmf/{f}", "r") as _file:
                file = _file.read()
                for name in form_names:
                    if name[0] in file and f[:-4].upper() != name[0].upper():
                        G.add_edge(f[:-4], name[0])
                        # print(f"{f[:-4]} -> {name[0]}")
        # pos = nx.circular_layout(G)
        # pos = nx.nx_agraph.pygraphviz_layout(G)
        # pos = nx.shell_layout(G)
        print(f"{len(G.edges.keys())} edges rendered")
        pos = nx.nx_agraph.graphviz_layout(G)
        plt.figure(1, (12, 9))
        nx.draw(G, with_labels=True, font_size=8, node_size=40, pos=pos, arrowsize=8, width=0.4, edge_color="grey")
        plt.savefig("depgraph.png")
        self.assertGreater(len(G.nodes), 10)

    def test_count_subs(self):
        pattern = re.compile("End Sub")
        subs = 0
        for f in os.listdir("./mmf/"):
            with open(f"./mmf/{f}", "r") as file:
                data = file.read()
                _subs = len(re.findall(pattern, data))
                subs += _subs
                print(f"{_subs} subs in {f}")
        print(subs, "subs total")
        self.assertGreater(subs, 100)
