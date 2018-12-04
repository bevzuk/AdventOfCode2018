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
