graph = [
    (5, 'A', 'D'),
    (7, 'A', 'B'),
    (9, 'B', 'D'),
    (15, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'F', 'E'),
    (11, 'F', 'G'),
    (9, 'G', 'E'),
    (5, 'E', 'C'),
    (7, 'E', 'B'),
    (8, 'B', 'C'),
]

graph.sort()

A = []

S = []

for edge in graph:
    if not (edge[1] in S and edge[2] in S):
        A.append(edge)
        S.append(edge[1])
        S.append(edge[2])

print A
print S