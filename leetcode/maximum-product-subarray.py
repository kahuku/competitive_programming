class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, ma, mi = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            lMa = max(ma * nums[i], nums[i], mi * nums[i])
            lMi = min(ma * nums[i], nums[i], mi * nums[i])

            ma = max(lMa, lMi)
            mi = min(lMi, lMa)

            res = max(res, ma)
        return res