n = int(input())
graph = {i + 1: [] for i in range(n)}
for i in range(n):
    numbers = input().split()
    for c in range(len(numbers)):
        if numbers[c] == '1':
            graph[i + 1].append(c + 1)
start, end = list(map(int, input().split()))


def BFS(graph, start, end):
    if end < 0 or end > len(graph):
        return -1
    visited = [False for i in range(n + 1)]
    distance = [-1 for i in range(n + 1)]
    queue = [start]
    visited[start] = True
    distance[start] = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                distance[v] = distance[u] + 1

    return distance[end]


print(BFS(graph, start, end))