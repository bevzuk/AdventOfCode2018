class Node:
    def __init__(self, name):
        self.name = name
        self.next = []
        self.prev = []

    def add_next(self, _next):
        self.next.append(_next)

    def add_prev(self, _prev):
        self.prev.append(_prev)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()
