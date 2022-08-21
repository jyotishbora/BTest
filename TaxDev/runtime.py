class Runtime:

    def __init__(self):
        self.list_items = dict()
        self.custom_items = dict()

    def set_list_item(self, *args):
        self.list_items[args[0]] = args[1:]

    def get_list_item(self, item):
        if item not in self.list_items:
            return None
        return self.list_items[item]

    def set_custom_item(self, key, value):
        self.custom_items[key] = value

    def get_custom_item(self, key):
        return self.custom_items[key]


if __name__ == "__main__":
    # run simple tests
    runtime = Runtime()
    runtime.set_list_item("a", "b", "c", "d")
    print(runtime.get_list_item("a"))
