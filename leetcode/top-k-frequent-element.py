from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return [item[0] for item in list(sorted(d.items(), key=lambda x: -x[1]))[0:k]]
        