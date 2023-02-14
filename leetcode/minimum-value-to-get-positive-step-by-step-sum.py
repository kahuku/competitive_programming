class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return (min(list(accumulate(nums, operator.add))) - 1) * -1 if min(list(accumulate(nums, operator.add))) < 0 else 1