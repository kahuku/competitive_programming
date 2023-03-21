from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        for pair in prerequisites:
            adjacency[pair[1]].append(pair[0])

        indegrees = [0] * numCourses
        for pair in prerequisites:
            indegrees[pair[0]] += 1

        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            courseNum = q.pop(0)
            for prereq in adjacency[courseNum]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)
        
        print(indegrees)
        return all(indegree == 0 for indegree in indegrees)