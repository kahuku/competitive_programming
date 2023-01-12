class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda num1, num2: num1 ^ num2, nums)