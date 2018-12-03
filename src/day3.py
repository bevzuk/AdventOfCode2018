class Piece:
    def __init__(self, s):
        split = s.split(' ')

        offset = split[2][:-1].split(',')
        self._top_offset = int(offset[0])
        self._left_offset = int(offset[1])

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

class FabricSolver:
    def Foo(self):
        print("Hello");
        return 0;