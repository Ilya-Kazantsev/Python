'''
Через рекурсию
def dfs(graph, x, y):
    graph[x][y] = 0
    width = len(graph)
    height = len(graph[0])
    for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if -1 < i < width and -1 < j < height and graph[i][j]:
            dfs(graph, i, j)
'''
def dfs(graph, x, y):
    queue = [(x, y)]
    width = len(graph)
    height = len(graph[0])
    while queue:
        x, y = queue.pop()
        graph[x][y] = 0
        for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if -1 < i < width and -1 < j < height and graph[i][j]:
                queue.append((i, j))


n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(n):
    graph[i] = [1 if j == '#' else 0 for j in input()]
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            count += 1
            dfs(graph, i, j)
print(count)