from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = defaultdict(int)
        for layer in wall:
            last_end = 0
            for i in range(len(layer)):
                last_end += layer[i]
                d[last_end] += 1

        return len(wall) - sorted(list(d.items()), reverse=True, key=lambda x: x[1])[1][1] if len(list(d.items())) != 1 else len(wall)