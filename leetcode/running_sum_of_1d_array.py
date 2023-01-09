class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i, num in enumerate(nums):
            if i == 0:
                runningSum.append(num)
            else:
                runningSum.append(num + runningSum[i - 1])
        return runningSum