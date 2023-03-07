# import collections
# def bfs(graph, root):
#     visited, queue = set(), collections.deque([root])
#     visited.add(root)
#     while queue:
#         vertex = queue.popleft()
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append(neighbour)
# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
#     breadth_first_search(graph, 0)


# Breadth First Search Поиск в ширину
def check_relation(net, first, second):
    graph = {}
    for edge in net:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    queue = [first]
    visited = {first}
    path = {first: None}

    while queue:
        node = queue.pop(0)
        if node == second:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = node
                print(path)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
