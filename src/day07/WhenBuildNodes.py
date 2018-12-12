import unittest

from src.day07.NodeBuilder import NodeBuilder


class WhenBuildNodes(unittest.TestCase):
    def test_it_has_single_child(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')
        nodes = nb.build()

        self.assertEqual('C', nodes[0].name)
        self.assertEqual('A', nodes[0].children[0].name)

    def test_it_has_two_children(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')
        nb.add('Step C must be finished before step B can begin.')
        nodes = nb.build()

        self.assertEqual('C', nodes[0].name)
        self.assertEqual(['A', 'B'], list(map(lambda x: x.name, nodes[0].children)))
