import heapq

class Prim:
    def __init__(self, graph):
        self.graph = graph
        # self.mst = []
        self.cost = 0
    
    def prim(self):
        visited = {}
        for k in self.graph.keys():
            visited[k] = False
        
        min_heap = [(0, list(self.graph.keys())[0])]
        while min_heap:
            cost, dest = heapq.heappop(min_heap)
            if not visited[dest]:
                visited[dest] = True
                # self.mst.append((dest, cost))
                self.cost += cost
                for n_cost, n in self.graph[dest]:
                    if not visited[n]:
                        heapq.heappush(min_heap, (n_cost, n))

n, e = map(int, input().split())
graph = {}
for _ in range(n):
    graph[input()] = []
for _ in range(e):
    a, b, cost = input().split()
    cost = int(cost)
    graph[a].append((cost, b))
    graph[b].append((cost, a))
solve = Prim(graph)
solve.prim()
print(solve.cost)