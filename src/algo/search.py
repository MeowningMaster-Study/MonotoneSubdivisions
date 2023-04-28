import math

import algo.chains
from primitives import Point, Edge
from typing import List
from numpy.linalg import norm
from numpy import array, cross


def find(point: Point, chains: algo.chains.Chains):
    for i, chain in enumerate(chains):
        for edge in chain:
            if point.y < edge.begin.y or point.y > edge.end.y:
                continue

            if isOnEdge(point, edge):
                return [i]

            pointVector = Point(point.x - edge.begin.x, point.y - edge.begin.y)
            pointRotation = math.atan2(pointVector.y, pointVector.x)

            if pointRotation > edge.rotation:
                if i == 0:
                    return []
                return [i - 1, i]
    return []


epsilon = 0.01


def isOnEdge(point: Point, edge: Edge):
    return abs(calcDistanceFromPointToEdge(point, edge)) < epsilon


def findOnEdge(point: Point, chain: List[Edge]):
    return next(findOnEdges(point, chain))


def findOnEdges(point: Point, chain: List[Edge]):
    return (edge for edge in chain if edge.begin.y <= point.y <= edge.end.y)


def findClosestEdge(point: Point, leftChain: List[Edge], rightChain: List[Edge]):
    minDistance = None
    minEdge = None

    for edge in findOnEdges(point, leftChain + rightChain):
        currentDistance = calcDistanceFromPointToEdge(point, edge)
        if minDistance is None or minDistance >= currentDistance:
            minDistance = currentDistance
            minEdge = edge

    return minEdge


def calcDistanceFromPointToEdge(point: Point, line: Edge):
    p1, p2, p3 = (
        array([point.x, point.y]),
        array([line.begin.x, line.begin.y]),
        array([line.end.x, line.end.y]),
    )
    return norm(cross(p2 - p1, p1 - p3)) / norm(p2 - p1)


def printResult(result: list[int], point: Point, chains: algo.chains.Chains):
    length = len(result)

    if length != 0:
        if length == 1:
            chain = result[0]
            print(
                f"The point is on the edge {findOnEdge(point, chains[chain])} of the chain {chain}"
            )
        else:
            first, second = result
            print(f"The point is between {first} and {second} chains")
            print(
                f"Closest edge is {findClosestEdge(point, chains[first], chains[second])}"
            )
    else:
        print("Point is outside")
