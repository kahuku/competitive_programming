# DOES NOT WORK -- ALMOST
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        new_edges = []
        restricted = set(restricted)
        for i in range(len(edges)):
            if edges[i][0] in restricted or edges[i][1] in restricted:
                continue
            edges[i].sort()
            new_edges.append(edges[i])
        
        new_edges.sort(key=lambda x: x[0])
        visited = set([0])
        last_count = -1
        count = 1

        while True:
            added = 0
            for edge in new_edges:
                if edge[0] not in visited and edge[1] not in visited:
                    continue
                elif edge[0] in visited and edge[1] not in visited:
                    visited.add(edge[1])
                    added += 1
                elif edge[1] in visited and edge[0] not in visited:
                    visited.add(edge[0])
                    added += 1

            if added == 0:
                break
        
        print(visited)
        return len(visited)
    
# THIS WORKS
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def add_reachable(start, visited, adj):
            for node in adj[start]:
                if node not in visited:
                    visited.add(node)
                    visited = add_reachable(node, visited, adj)
            return visited

        adj = defaultdict(list)
        restricted = set(restricted)
        for edge in edges:
            if edge[0] in restricted or edge[1] in restricted:
                continue
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set([0])
        visited = add_reachable(0, visited, adj)
        return len(visited)