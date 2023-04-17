from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i in range(len(nums)):
            s = sum([int(str(nums[i])[j]) for j in range(len(str(nums[i])))])
            d[s].append(nums[i])
        
        m = -1
        groups = list(d.values())
        for i in range(len(groups)):
            group = groups[i]
            if len(group) < 2: continue
            group.sort(reverse=True)
            m = max(m, group[0] + group[1])

        return m