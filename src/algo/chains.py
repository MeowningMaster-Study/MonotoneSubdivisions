import algo.edges

from primitives import Point, Edge, VertexEdges
from typing import List

Chains = List[List[Edge]]


def build(vertices: List[Point], verticesEdges: List[VertexEdges]) -> Chains:
    sortedOutEdges: List[List[Edge]] = [
        algo.edges.sort(vertexEdges.out) for vertexEdges in verticesEdges
    ]

    countOfChains = algo.edges.sumWeight(sortedOutEdges[0])
    chains = []

    for i in range(countOfChains):
        chain = []
        currentVertex = 0
        lastVertex = len(sortedOutEdges) - 1
        while currentVertex != lastVertex:
            # leftmost unused
            edge = next(x for x in sortedOutEdges[currentVertex] if x.weight > 0)
            chain.append(edge)
            edge.weight -= 1
            currentVertex = vertices.index(edge.end)
        chains.append(chain)
    return chains


def printResult(vertices: List[Point], chains: Chains):
    print("Chains:")
    for i, chain in enumerate(chains):
        print(f"* {i}: {vertices.index(chain[0].begin)}", end="")
        for edge in chain:
            print(f" {vertices.index(edge.end)}", end="")
        print()
