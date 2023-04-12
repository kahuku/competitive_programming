class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set([(p[0], p[1]) for p in points])
        m = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2 and (x1, y2) in points and (x2, y1) in points:
                    m = min(m, abs(x2 - x1) * abs(y2 - y1))
        return m if m != float('inf') else 0