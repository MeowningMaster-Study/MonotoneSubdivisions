from typing import List, Tuple
from primitives import Point, Edge


def vertices(rawVertices: List[Tuple[int, int]]) -> List[Point]:
    return [Point(x, y) for (x, y) in rawVertices]


def edges(rawEdges: List[Tuple[int, int]], vertices: List[Point]) -> List[Edge]:
    return [Edge(vertices[a], vertices[b]) for (a, b) in rawEdges]


def point(rawPoint: Tuple[int, int]) -> Point:
    return Point(rawPoint[0], rawPoint[1])
