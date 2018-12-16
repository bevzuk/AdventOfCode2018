from src.day07.Elf import Elf
from src.day07.NodeBuilder import NodeBuilder


def route(nodes):
    _route = ""
    _nodes = list(nodes)
    _completed = set()

    while len(_nodes) > 0:
        node = sorted(_nodes, key=lambda x: x.name).pop(0)
        _route += node.name
        _completed.add(node)
        _nodes.remove(node)
        _nodes_to_add = filter(lambda x: set(x.prev).issubset(_completed), node.next)
        _nodes.extend(_nodes_to_add)

    return _route


def nothing_to_do(elves):
    _result = True
    for elf in elves:
        if elf.has_work_to_do():
            _result = False
    return _result


def print_line(second, elves, completed):
    s = ""
    s += str(second) + "\t"
    for elf in elves:
        if elf.has_work_to_do():
            s += elf.work_in_progress.name
        else:
            s += '.'
        s += "\t"
    for node in completed:
        s += node.name
    print(s)


def work(nodes, elves):
    _second = 0
    _nodes = list(nodes)
    _completed = []

    while True:
        for elf in elves:
            elf.work()
            if not elf.has_work_to_do():
                if elf.completed_work is not None:
                    _completed.append(elf.completed_work)
                    _nodes_to_add = filter(lambda x: set(x.prev).issubset(_completed), elf.completed_work.next)
                    _nodes.extend(_nodes_to_add)
                    elf.completed_work = None
                if len(_nodes) > 0:
                    node = sorted(_nodes, key=lambda x: x.name).pop(0)
                    elf.assign(node)
                    _nodes.remove(node)

        print_line(_second, elves, _completed)
        _second += 1

        if nothing_to_do(elves):
            break


nb = NodeBuilder()
with open('day07.input.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    nb.add(line)
root = nb.build()

print("part 1:", route(root))

work(root, [Elf(), Elf(), Elf(), Elf(), Elf()])
