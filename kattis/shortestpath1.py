import heapq
from collections import defaultdict

numNodes, numEdges, numQueries, startNode = map(int, input().split())
while numNodes != 0 or numEdges != 0 or numQueries != 0 or startNode != 0:
    adjMat = defaultdict(list)
    for _ in range(numEdges):
        inNode, outNode, weight = map(int, input().split())
        adjMat[inNode].append((outNode, weight))

    # Dijkstra's algorithm
    dists = [float('inf') for _ in range(numNodes)]
    dists[startNode] = 0
    sptSet = [False] * numNodes
    pq = [(0, startNode)]  # Priority queue with (distance, node) tuples
    while pq:
        dist, u = heapq.heappop(pq)
        if sptSet[u]:
            continue
        sptSet[u] = True
        for v, w in adjMat[u]:
            if not sptSet[v] and dist + w < dists[v]:
                dists[v] = dist + w
                heapq.heappush(pq, (dists[v], v))
    # End of Dijkstra's algorithm

    for _ in range(numQueries):
        targetNode = int(input())
        print(dists[targetNode] if dists[targetNode] != float('inf') else 'Impossible')

    print()
    numNodes, numEdges, numQueries, startNode = map(int, input().split())