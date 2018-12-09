import csv

with open('day06.input.txt', 'r') as f:
    coordinates = list(map(lambda x: [int(x[0]), int(x[1])], list(csv.reader(f))))

# coordinates = [
#     [1, 1],
#     [1, 6],
#     [8, 3],
#     [3, 4],
#     [5, 5],
#     [8, 9]]

size_x = max(list(map(lambda x: x[0], coordinates)))
size_y = max(list(map(lambda x: x[1], coordinates)))


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def distance_to_coordinates(x, y):
    distances = []
    for c in coordinates:
        distances.append(distance([x, y], c))
    return distances


def calculate_map():
    map = [[None for x in range(size_x)] for y in range(size_y)]
    for x in range(0, size_x):
        for y in range(0, size_y):
            distances = distance_to_coordinates(x, y)
            min_distance = min(distances)
            if sum(1 if d == min_distance else 0 for d in distances) == 1:
                map[y][x] = distances.index(min_distance)
    return map


def remove_infinities(map):
    infinities = set()
    for x in range(size_x):
        if map[0][x] is not None:
            infinities.add(map[0][x])
        if map[size_y - 1][x] is not None:
            infinities.add(map[size_y - 1][x])
    for y in range(size_y):
        if map[y][0] is not None:
            infinities.add(map[y][0])
        if map[y][size_x - 1] is not None:
            infinities.add(map[y][size_x - 1])
    for x in range(size_x):
        for y in range(size_y):
            if map[y][x] in infinities:
                map[y][x] = None
    return map


def calculate_counts(map):
    counts = {}
    for x in range(size_x):
        for y in range(size_y):
            if map[y][x] is not None:
                if map[y][x] in counts:
                    counts[map[y][x]] += 1
                else:
                    counts[map[y][x]] = 1
    return counts


def task_1():
    map = calculate_map()
    map = remove_infinities(map)
    counts = calculate_counts(map)
    return max(counts.values())


def task_2():
    map = [[None for x in range(size_x)] for y in range(size_y)]
    for x in range(0, size_x):
        for y in range(0, size_y):
            distances = distance_to_coordinates(x, y)
            if sum(distances) < 10000:
                map[y][x] = 1
    s = 0
    for x in range(0, size_x):
        for y in range(0, size_y):
            if map[y][x] is not None:
                s += map[y][x]
    return s


print(task_1())
print(task_2())
