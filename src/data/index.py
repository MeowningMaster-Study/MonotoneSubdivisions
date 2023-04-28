import data.raw as raw
import data.prepare as prepare

vertices = prepare.vertices(raw.vertices)
edges = prepare.edges(raw.edges, vertices)
point = prepare.point(raw.point)
