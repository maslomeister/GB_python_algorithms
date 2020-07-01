# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


import random

def dfs(graph, vertex, visited):
    visited.append(vertex)

    for v in graph[vertex]:
        if v not in visited:
            dfs(graph, v, visited)

    return visited


def rollDice():
    roll = random.randint(1, 100)

    if roll <= 50:
        return False
    elif roll >= 51:
        return True


def create_graph(vertices):

    graph = {}

    for i in range(vertices):
        graph[i] = set()

    unconnected_vertices = [i for i in range(1, vertices)]

    connected_vertices = [0]

    random.shuffle(unconnected_vertices)

    choosen_number = unconnected_vertices.pop()

    graph[0].add(choosen_number)

    connected_vertices.append(choosen_number)

    while len(unconnected_vertices) > 0:

        random.shuffle(unconnected_vertices)
        random.shuffle(connected_vertices)

        if rollDice:

            from_vert = connected_vertices[0]

            to_vert = unconnected_vertices.pop()

            graph[from_vert].add(to_vert)

            connected_vertices.append(to_vert)

        else:

            from_vert = unconnected_vertices.pop()

            to_vert = connected_vertices[0]

            graph[from_vert].add(to_vert)

            connected_vertices.append(from_vert)

    return graph


ver = int(input("\nВведите количество вершин: "))

g = create_graph(ver)
graph = dict(sorted(g.items()))
print("\nСписок смежности: ")
for key, val in graph.items():
    if val != set():
        print(f"{key} : {val}")
    else:
        print(f"{key} : {{}}")
    print("")

print(dfs(graph, 0, []))
