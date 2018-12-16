from src.day07.NodeBuilder import NodeBuilder


def route(nodes):
    _route = ""
    _nodes = set(nodes)
    _completed = set()

    while len(_nodes) > 0:
        node = sorted(_nodes, key=lambda x: x.name).pop(0)
        _route += node.name
        _completed.add(node)
        _nodes.remove(node)
        _nodes_to_add = set(filter(lambda x: set(x.prev).issubset(_completed), node.next))
        _nodes = _nodes.union(_nodes_to_add)

    return _route


nb = NodeBuilder()
with open('day07.input.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    nb.add(line)
root = nb.build()

print("part 1:", route(root))
