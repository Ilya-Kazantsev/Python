n = int(input())

graph = {i: {} for i in range(n)}

for i in range(n):
    values = list(map(int, input().split()))
    for j in range(n):
        if values[j] > 0:
            graph[i][j] = values[j]

s, f = list(map(int, input().split()))


def dijkstra(graph, start, finish):
    distance = [1e10 for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    # Для восстановления маршрута
    path = [-1 for i in range(len(graph))]
    distance[start] = 0
    for _ in range(len(graph)):
        v = -1
        for i in range(len(distance)):
            if not visited[i] and (v == -1 or distance[i] < distance[v]):
                v = i
        visited[v] = True
        # Релаксация рёбер
        for key, value in graph[v].items():
            if distance[v] + value < distance[key]:
                distance[key] = distance[v] + value
                path[key] = v

    # Восстановление пути
    route = []
    v = finish
    while v != start:
        route.append(v + 1)
        v = path[v]
    route.append(start)
    route.reverse()

    return distance[finish], route


result = dijkstra(graph, s - 1, f - 1)

if result[0] == 1e10:
    print(-1)
else:
    print(result[0])
    print(*result[1])
