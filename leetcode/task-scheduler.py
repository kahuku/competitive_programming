from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxJobCount, maxJobCountCount = 0, 0
        d = defaultdict(int)
        for task in tasks:
            d[task] += 1
            if d[task] == maxJobCount: maxJobCountCount += 1
            elif d[task] > maxJobCount: maxJobCount, maxJobCountCount = d[task], 1
        partCount = maxJobCount - 1
        partLength = n - maxJobCountCount + 1
        emptySlots = partCount * partLength
        otherTasks = len(tasks) - (maxJobCount * maxJobCountCount)
        numIdles = max(0, emptySlots - otherTasks)
        return len(tasks) + numIdles