class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums.append(nums[i])
        for i in range(n):
            if nums[i] == 1:
                nums.append(nums[i])
        for i in range(n):
            if nums[i] == 2:
                nums.append(nums[i])
        nums[:] = nums[n:]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        nums[:] = [0] * d[0] + [1] * d[1] + [2] * d[2]