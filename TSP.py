# Travelling Salesman Problem (TSP)

n = 4

# Distance matrix
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * n
visited[0] = True

min_cost = float('inf')
best_path = []

def tsp(city, count, current_cost, path):
    global min_cost, best_path

    if count == n:
        total_cost = current_cost + cost[city][0]

        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path + [0]
        return

    for next_city in range(n):
        if not visited[next_city]:
            visited[next_city] = True

            tsp(
                next_city,
                count + 1,
                current_cost + cost[city][next_city],
                path + [next_city]
            )

            visited[next_city] = False

tsp(0, 1, 0, [0])

print("Shortest Path:", " -> ".join(map(str, best_path)))
print("Minimum Cost:", min_cost)
