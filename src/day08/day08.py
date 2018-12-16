from src.day08.Node import Node

with open('day08.input.txt', 'r') as f:
    data = [int(x) for x in f.read().split(' ')]


def build(data, ind):
    number_of_childen = data[ind]
    number_of_metadata = data[ind + 1]
    node = Node()
    ind += 2
    for i in range(number_of_childen):
        (child, ind) = build(data, ind)
        node.add_child(child)
    for i in range(number_of_metadata):
        node.add_metadata(data[ind + i])
    # print(node.metadata, ind + number_of_metadata)
    return (node, ind + number_of_metadata)


print(data)

i = 0
(root, i) = build(data, i)

print("task 1:", root.sum())
print("task 2:", root.sum2())
