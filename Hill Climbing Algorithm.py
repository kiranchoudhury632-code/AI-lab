def hill_climbing(graph, start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])

        if not neighbors:
            break

        # Select the neighbor with the highest value
        next_node = max(neighbors, key=lambda x: x[1])

        if next_node[1] <= graph.get(current + "_value", [(0, 0)])[0][1]:
            break

        current = next_node[0]
        path.append(current)

    return path


# Graph with heuristic values
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 3)],
    'D': [('G', 8)],
    'E': [('G', 6)],
    'F': [('G', 7)],
    'G': []
}

# Simple Hill Climbing
current = 'A'
goal = 'G'
path = [current]

while current != goal:
    neighbors = graph[current]

    if not neighbors:
        break

    next_node, value = max(neighbors, key=lambda x: x[1])

    current = next_node
    path.append(current)

print("Path:", " -> ".join(path))
