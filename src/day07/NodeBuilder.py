import re

from src.day07.Node import Node


class NodeBuilder:
    def __init__(self):
        self.nodes = {}

    def add(self, s):
        m = re.match('Step (.*) must be finished before step (.*) can begin.', s)
        first_node = Node(m.group(1))
        second_node = Node(m.group(2))
        first_node.add_child(second_node)
        if first_node.name in self.nodes:
            self.nodes[first_node.name].append(second_node)
        else:
            self.nodes[first_node.name] = [second_node]

    def build(self):
        return list(map(lambda x: Node(x, self.nodes[x]), self.nodes.keys()))
