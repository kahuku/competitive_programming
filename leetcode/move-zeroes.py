class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fill_indx, n = 0, len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[fill_indx] = nums[i]
                fill_indx += 1
        for i in range(fill_indx, n):
            nums[i] = 0