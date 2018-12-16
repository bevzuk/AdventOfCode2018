class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, m):
        self.metadata.append(m)

    def sum(self):
        s = 0
        for m in self.metadata:
            s += m
        for c in self.children:
            s += c.sum()
        return s

    def sum2(self):
        s = 0
        if self.children:
            for m in self.metadata:
                if m <= len(self.children):
                    s += self.children[m - 1].sum2()
        else:
            for m in self.metadata:
                s += m
        return s
