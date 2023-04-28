from primitives import Edge, Point, VertexEdges
from typing import List


def buildVerticesEdges(vertices: List[Point], edges: List[Edge]) -> List[VertexEdges]:
    result = [VertexEdges() for i in range(len(vertices))]
    for edge in edges:
        result[vertices.index(edge.end)]._in.append(edge)
        result[vertices.index(edge.begin)].out.append(edge)
    return result


def sumWeight(edges: List[Edge]) -> int:
    return sum(edge.weight for edge in edges)


def sort(edges: List[Edge]) -> List[Edge]:
    return sorted(edges, key=lambda edge: edge.rotation, reverse=True)


def findLeftmost(edges: List[Edge]) -> Edge:
    return max(edges, key=lambda edge: edge.rotation)
