class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 1
        points.sort(key=lambda x: x[1])
        shootAt = points[0][1]
        for point in points:
            if point[0] <= shootAt:
                continue
            arrows += 1
            shootAt = point[1]
        return arrows