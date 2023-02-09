class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = sorted(nums)
        out = []
        for i in range(len(nums)):
            out.append(d.index(nums[i]))
        return out

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = [0 for _ in range(101)]
        for num in nums:
            d[num] += 1
        for i in range(1, len(d)):
            d[i] += d[i - 1]
        out = []
        for i in range(len(nums)):
            if nums[i] == 0:
                out.append(0)
            else:
                out.append(d[nums[i] - 1])
        return out