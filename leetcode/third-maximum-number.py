class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        u = set(nums)
        l = sorted(list(u))
        return l[-3] if len(l) > 2 else l[-1]