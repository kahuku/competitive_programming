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
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = nums[0], nums[0]
        final_max = nums[0]
        for i in range(1, len(nums)):
            curr_max, curr_min = max(nums[i], nums[i] * curr_max, nums[i] * curr_min), min(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            final_max = max(final_max, curr_max)
        return final_max