n, s, f = list(map(int, input().split()))

graph = {i: {} for i in range(n)}

for i in range(n):
    values = list(map(int, input().split()))
    for j in range(n):
        if values[j] > 0:
            graph[i][j] = values[j]


def dijkstra(graph, start):
    distance = [1e10 for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
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
    return distance


result = dijkstra(graph, s - 1)[f - 1]

if result == 1e10:
    print(-1)
else:
    print(result)