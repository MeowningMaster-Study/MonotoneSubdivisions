import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.weightIn = 0
        self.weightOut = 0

    def __repr__(self):
        return str(f"({str(self.x)}, {str(self.y)})")

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class VertexEdges:
    def __init__(self):
        self.out = []
        self._in = []


class Edge:
    def __init__(self, begin: Point, end: Point):
        self.begin = begin
        self.end = end

        self.weight = 1

        self.rotation = math.atan2(end.y - begin.y, end.x - begin.x)

    def __repr__(self):
        return str(f"({str(self.begin)}, {str(self.end)})")

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.begin == other.begin and self.end == other.end
        return False
