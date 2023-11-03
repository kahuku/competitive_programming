from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        for ke in d.keys():
            for i in range(1, len(d[ke])):
                if d[ke][i] - d[ke][i - 1] <= k:
                    return True
        return False