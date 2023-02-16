n = int(input())

graph = {i: [] for i in range(n)}

for i in range(n):
    values = list(map(int, input().split()))
    for j in range(n):
        if values[j] > 0:
            graph[i].append(j)

s, f = list(map(int, input().split()))


# Просто подсчёт
def get_paths_count(graph, current, target, visited, path):
    visited[current] = True
    path.append(current)
    if current == target:
        paths.append(path.copy())
    else:
        for v in graph[current]:
            if not visited[v]:
                get_paths_count(graph, v, target, visited, path)
    path.pop()
    visited[current] = False


def get_all_paths(graph, start, finish):
    def generate_all_paths(graph, current, target, visited, path):
        visited[current] = True
        path.append(current)
        if current == target:
            paths.append(path.copy())
        else:
            for v in graph[current]:
                if not visited[v]:
                    generate_all_paths(graph, v, target, visited, path)
        path.pop()
        visited[current] = False
    paths = []
    visited = [False for i in range(len(graph))]
    generate_all_paths(graph, start, finish, visited, [])
    return paths


paths = get_all_paths(graph, 0, 9)
print(*[[i, paths[i]] for i in range(len(paths))], sep='\n')
