class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i, num in enumerate(nums):
            if i == 0:
                runningSum.append(num)
            else:
                runningSum.append(num + runningSum[i - 1])
        return runningSum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[i - 1])
        return sums

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[0:i + 1]) for i in range(len(nums))]