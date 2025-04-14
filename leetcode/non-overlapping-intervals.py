class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        taken = 1
        last_taken = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[last_taken][1]:
                print("taking", intervals[i])
                taken += 1
                last_taken = i
        return len(intervals) - taken