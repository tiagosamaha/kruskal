from kruskal import kruskal

vertexs = ['A', 'B', 'C', 'D']
edges = [
    (1, 'A', 'B'),
    (5, 'A', 'C'),
    (3, 'A', 'D'),
    (4, 'B', 'C'),
    (2, 'B', 'D'),
    (1, 'C', 'D'),
]

print kruskal(vertexs, edges)
