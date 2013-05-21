from kruskal import kruskal

vertexs = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    (5, 'A', 'B'),
    (1, 'A', 'F'),
    (2, 'A', 'D'),
    (3, 'B', 'C'),
    (3, 'B', 'E'),
    (1, 'C', 'D'),
    (4, 'C', 'F'),
    (4, 'D', 'E'),
    (2, 'E', 'F'),
]

print kruskal(vertexs, edges)
