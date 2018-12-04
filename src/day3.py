import array


class Piece:
    def __init__(self, s):
        split = s.split(' ')

        offset = split[2][:-1].split(',')
        self._left_offset = int(offset[0])
        self._top_offset = int(offset[1])

        size = split[3].split('x')
        self._width = int(size[0])
        self._height = int(size[1])

    @property
    def top_offset(self):
        return self._top_offset

    @property
    def left_offset(self):
        return self._left_offset

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

class Fabric:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = []
        for row in range(0, height):
            self._area.append([])
            for column in range(0, width):
                self._area[row].append(0)

    def Claim(self, piece):
        for row in range(0, piece.height):
            for column in range(0, piece.width):
                self._area[piece.top_offset + row][piece.left_offset + column] += 1

    def Area(self):
        area = "\n"
        for row in range(0, self._height):
            for column in range(0, self._width):
                if self._area[row][column] == 0:
                    area += "."
                else:
                    area += str(self._area[row][column])
            area += '\n'
        return area

    @property
    def OverlappingInches(self):
        overlappingInches = 0
        for row in range(0, self._height):
            for column in range(0, self._width):
                if self._area[row][column] > 1:
                    overlappingInches += 1
        return overlappingInches


text_file = open("day3.input.txt", "r")
pieces = list(map(lambda x: Piece(x.replace("\n", "")), text_file.readlines()))

max_width = 0
max_height = 0
for piece in pieces:
    if piece.left_offset + piece.width > max_width:
        max_width = piece.left_offset + piece.width
    if piece.top_offset + piece.height > max_height:
        max_height = piece.top_offset + piece.height

fabric = Fabric(max_width, max_height)
for piece in pieces:
    fabric.Claim(piece)

print(fabric._width)
print(fabric._height)
print(fabric.OverlappingInches)

out_file = open("day3.out.txt", "w")
out_file.write(fabric.Area())
out_file.close()

