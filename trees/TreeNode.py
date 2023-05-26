class TreeNode:
    def __init__(self, name, designation):
        self.data = { "name": name, "designation": designation }
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, key, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if key == "both":
            print(prefix + self.data["name"] + " (" + self.data["designation"] + ")")
        else:
            print(prefix + self.data[key])
        if self.children:
            for child in self.children:
                child.print_tree(key, level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)