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
