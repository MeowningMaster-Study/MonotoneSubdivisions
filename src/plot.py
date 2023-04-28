from matplotlib import pyplot as plt

from typing import List
from primitives import Point, Edge


def plot(vertices: List[Point], edges: List[Edge], point: Point):
    ax = plt.axes()

    for i, vertex in enumerate(vertices):
        plt.annotate(i, (vertex.x, vertex.y))
        plt.plot(vertex.x, vertex.y, marker="o", markerfacecolor="black")

    for e in edges:
        ax.arrow(e.begin.x, e.begin.y, e.end.x - e.begin.x, e.end.y - e.begin.y)
        plt.annotate(
            e.weight, xy=((e.end.x + e.begin.x) / 2, (e.end.y + e.begin.y) / 2)
        )

    plt.plot(point.x, point.y, marker="o")
    plt.show()
