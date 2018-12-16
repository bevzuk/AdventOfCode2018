import re

from src.day07.Node import Node


class NodeBuilder:
    def __init__(self):
        self.nodes = {}

    def add(self, s):
        m = re.match('Step (.*) must be finished before step (.*) can begin.', s)
        first_node = self.get_node(m.group(1))
        second_node = self.get_node(m.group(2))
        first_node.add_next(second_node)
        second_node.add_prev(first_node)

    def get_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]

    def build(self):
        heads = []
        for node in self.nodes.values():
            if not node.prev:
                heads.append(node)
        return heads
