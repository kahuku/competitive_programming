from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = defaultdict(set)
        for p, d in prerequisites:
            pre[p].add(d)
        
        adj = [set() for _ in range(numCourses)]
        visited = set()

        def dfs(node):
            if node in visited:
                return adj[node]
            visited.add(node)
            for neigh in pre[node]:
                adj[node].add(neigh)
                adj[node].update(dfs(neigh))
            return adj[node]

        for node in range(numCourses):
            dfs(node)

        return [v in adj[u] for u, v in queries]
