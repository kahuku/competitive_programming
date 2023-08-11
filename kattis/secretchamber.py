def can_transform(graph, word1, word2):
    if len(word1) != len(word2): return False

    for a, b in zip(word1, word2):
        if not has_path(graph, a, b): return False
    return True

def has_path(graph, a, b, visited=None):
    if visited is None:  visited = set()

    if a == b: return True

    visited.add(a)

    if a not in graph: return False

    for neighbor in graph[a]:
        if neighbor not in visited and has_path(graph, neighbor, b, visited): return True
    return False

n_pairs, n_words = map(int, input().split())
graph = {}
for _ in range(n_pairs):
    a, b = input().split()
    graph.setdefault(a, [])
    graph[a].append(b)
for _ in range(n_words):
    a, b = input().split()
    print("yes" if can_transform(graph, a, b) else "no")