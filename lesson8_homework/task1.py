# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


graph = []

size = int(input("\nУкажите количество друзей: "))

graph = [[0 if i == j else 1 for j in range(size)] for i in range(size)]

print("\nМатрица смежности: ")
print(*graph, sep="\n")


def calc_handshakes(graph):
    handshakes = 0

    for i in range(len(graph)):
        handshakes += sum(graph[i])

    return handshakes // 2


print(f"\nКоличество рукопожатий: {calc_handshakes(graph)}")
