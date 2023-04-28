import algo.edges

from primitives import Point, VertexEdges
from typing import List


def up(vertices: List[Point], verticesEdges: List[VertexEdges]):
    lastIndex = len(vertices) - 1
    for i, vertex in enumerate(vertices):
        if i == 0 or i == lastIndex:
            continue

        vertex.weightIn = algo.edges.sumWeight(verticesEdges[i]._in)
        vertex.weightOut = algo.edges.sumWeight(verticesEdges[i].out)

        if vertex.weightIn > vertex.weightOut:
            leftEdge = algo.edges.findLeftmost(verticesEdges[i].out)
            leftEdge.weight = vertex.weightIn - vertex.weightOut + leftEdge.weight


def down(vertices: List[Point], verticesEdges: List[VertexEdges]):
    lastIndex = len(vertices) - 1
    for i, vertex in reversed(list(enumerate(vertices))):
        if i == 0 or i == lastIndex:
            continue

        vertex.weightIn = algo.edges.sumWeight(verticesEdges[i]._in)
        vertex.weightOut = algo.edges.sumWeight(verticesEdges[i].out)

        if vertex.weightOut > vertex.weightIn:
            leftEdge = algo.edges.findLeftmost(verticesEdges[i]._in)
            leftEdge.weight = vertex.weightOut - vertex.weightIn + leftEdge.weight


def full(vertices: List[Point], verticesEdges: List[VertexEdges]):
    up(vertices, verticesEdges)
    down(vertices, verticesEdges)
