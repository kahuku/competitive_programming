from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        l = sorted(d.items(), key=lambda x: x[1], reverse=True)
        l = [item[0] for item in l if item[1] > (len(nums) // 3)]
        return l