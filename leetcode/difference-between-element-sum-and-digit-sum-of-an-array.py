class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el = sum(nums)
        di = 0
        for num in nums:
            for digit in str(num):
                di += int(digit)
        return el - di if el - di > 0 else di - el