class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        k %= len(nums)
        a = nums[-1*k:]
        a.extend(nums[:-1*k])
        for i in range(len(nums)):
            nums[i] = a[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a , n= nums.copy(), len(nums)
        for i in range(n):
            ind = (i + k) % n
            nums[ind] = a[i]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums);nums[:] = nums[-k:] + nums[:-k]