class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        arr = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= arr[-1][1]:
                arr[-1][1] = max(intervals[i][1], arr[-1][1])
            else:
                arr.append(intervals[i])
        return arr