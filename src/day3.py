class Piece:
    def __init__(self, s):
        split = s.replace("\n", "").split(' ')

        self.number = int(split[0][1:])

        offset = split[2][:-1].split(',')
        self._left_offset = int(offset[0])
        self._top_offset = int(offset[1])

        size = split[3].split('x')
        self._width = int(size[0])
        self._height = int(size[1])

        self.Corners = [
            (self.left_offset, self.top_offset),
            (self.left_offset + self.width - 1, self.top_offset),
            (self.left_offset + self.width - 1, self.top_offset + self.height - 1),
            (self.left_offset, self.top_offset + self.height - 1)
        ]

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

    def overlaps(self, piece):
        for corner in piece.Corners:
            if self.contains(corner):
                return True

        for corner in self.Corners:
            if piece.contains(corner):
                return True

        return False

    def contains(self, point):
        return self.left_offset <= point[0] < self.left_offset + self.width and \
               self.top_offset <= point[1] < self.top_offset + self.height


class Fabric:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = []
        for row in range(0, height):
            self._area.append([])
            for column in range(0, width):
                self._area[row].append(0)

    def claim(self, piece):
        for row in range(0, piece.height):
            for column in range(0, piece.width):
                self._area[piece.top_offset + row][piece.left_offset + column] += 1

    def area(self):
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
    def overlapping_inches(self):
        _overlapping_inches = 0
        for row in range(0, self._height):
            for column in range(0, self._width):
                if self._area[row][column] > 1:
                    _overlapping_inches += 1
        return _overlapping_inches


def solve_part_1():
    text_file = open("day3.input.txt", "r")
    pieces = list(map(lambda x: Piece(x), text_file.readlines()))
    text_file.close()

    max_width = 0
    max_height = 0
    for piece in pieces:
        if piece.left_offset + piece.width > max_width:
            max_width = piece.left_offset + piece.width
        if piece.top_offset + piece.height > max_height:
            max_height = piece.top_offset + piece.height

    fabric = Fabric(max_width, max_height)
    for piece in pieces:
        fabric.claim(piece)

    print("1. Number of overlapping inches: ", fabric.overlapping_inches)

    # out_file = open("day3.out.txt", "w")
    # out_file.write(fabric.Area())
    # out_file.close()


def solve_part_2():
    text_file = open("day3.input.txt", "r")
    pieces = list(map(lambda x: Piece(x), text_file.readlines()))
    text_file.close()

    for piece1 in pieces:
        overlaps = False
        for piece2 in pieces:
            if piece1 == piece2:
                continue
            if piece1.overlaps(piece2):
                overlaps = True
                continue
        if not overlaps:
            print("2. Non-overlapping piece:", piece1.number)


# solve_part_1()
solve_part_2()
