class Node:
    def __init__(self, name, child=[]):
        self.name = name
        self.children = child

    def add_child(self, child):
        self.children.append(child)
