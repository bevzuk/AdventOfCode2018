import unittest

from src.day07.NodeBuilder import NodeBuilder
from src.day07.day07 import route


class WhenBuildNodes(unittest.TestCase):
    def test_it_has_single_next(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')

        root_node = nb.build()[0]

        self.assertEqual('C', root_node.name)
        self.assertEqual('A', root_node.next[0].name)

    def test_it_has_no_prev(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')

        root_node = nb.build()[0]

        self.assertEqual([], root_node.prev)
        self.assertEqual('C', root_node.next[0].prev[0].name)

    def test_it_has_two_next(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')
        nb.add('Step C must be finished before step B can begin.')

        root_node = nb.build()[0]

        self.assertEqual('C', root_node.name)
        self.assertEqual(['A', 'B'], list(map(lambda x: x.name, root_node.next)))

    def test_it_has_next_after_next(self):
        nb = NodeBuilder()
        nb.add('Step A must be finished before step B can begin.')
        nb.add('Step B must be finished before step C can begin.')

        root_node = nb.build()[0]

        self.assertEqual('A', root_node.name)
        self.assertEqual(['B'], list(map(lambda x: x.name, root_node.next)))
        self.assertEqual(['C'], list(map(lambda x: x.name, root_node.next[0].next)))

    def test_it_forms_romb(self):
        nb = NodeBuilder()
        nb.add('Step A must be finished before step B can begin.')
        nb.add('Step A must be finished before step C can begin.')
        nb.add('Step B must be finished before step D can begin.')
        nb.add('Step C must be finished before step D can begin.')

        root_node = nb.build()[0]

        self.assertEqual('A', root_node.name)
        self.assertEqual(['B', 'C'], list(map(lambda x: x.name, root_node.next)))
        self.assertEqual(['D'], list(map(lambda x: x.name, root_node.next[0].next)))
        self.assertEqual(['D'], list(map(lambda x: x.name, root_node.next[1].next)))

    def test_it_calculates_route(self):
        nb = NodeBuilder()
        nb.add('Step C must be finished before step A can begin.')
        nb.add('Step C must be finished before step F can begin.')
        nb.add('Step A must be finished before step B can begin.')
        nb.add('Step A must be finished before step D can begin.')
        nb.add('Step B must be finished before step E can begin.')
        nb.add('Step D must be finished before step E can begin.')
        nb.add('Step F must be finished before step E can begin.')

        root_node = nb.build()

        self.assertEqual('CABDFE', route(root_node))
