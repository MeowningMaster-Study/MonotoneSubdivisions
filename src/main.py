import data.index as data
import plot
import algo.balance, algo.edges, algo.chains, algo.search

vertices = sorted(data.vertices, key=lambda vertex: vertex.y)
edges = data.edges
point = data.point
verticesEdges = algo.edges.buildVerticesEdges(vertices, edges)

algo.balance.full(vertices, verticesEdges)
plot.plot(vertices, edges, point)

chains = algo.chains.build(vertices, verticesEdges)
result = algo.search.find(point, chains)

algo.chains.printResult(vertices, chains)
algo.search.printResult(result, point, chains)
