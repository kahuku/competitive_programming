class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = list(accumulate(nums, operator.add))
        for i in range(len(nums)):
            left = pre[i-1] if i else 0
            right = pre[len(nums) - 1] - pre[i] if i != len(nums) - 1 else 0
            if left == right:
                return i
        return -1