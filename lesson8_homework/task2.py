# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float("inf")] * length
    parent = [-1] * length

    paths = {}
    for i in range(length):
        paths[i] = []

    cost[start] = 0
    min_cost = 0

    while min_cost < float("inf"):

        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float("inf")

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(length):

        if is_visited[i]:
            paths[i].append(i)
            temp_i = i

            while parent[temp_i] != -1:
                paths[i].append(parent[temp_i])
                temp_i = parent[temp_i]

    return cost, paths


s = int(input("\nОт какой вершины идти: "))
results = dijkstra(g, s)
print(f"\n{results[0]}\n")
for k, v in results[1].items():
    print(k, v)