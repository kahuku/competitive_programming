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

from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        nums[:] = [0] * d[0] + [1] * d[1] + [2] * d[2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergesort(arr, l_i, r_i):
            if l_i < r_i:
                mid = (r_i - l_i) // 2 + l_i
                mergesort(arr, l_i, mid)
                mergesort(arr, mid + 1, r_i)
                merge(arr, l_i, mid, r_i)

        def merge(arr, l, mid, r):
            left = arr[l:mid+1]
            right = arr[mid+1:r+1]
            l_i, r_i, arr_i = 0, 0, l
            while l_i < len(left) and r_i < len(right):
                if left[l_i] < right[r_i]:
                    arr[arr_i] = left[l_i]
                    l_i += 1
                else:
                    arr[arr_i] = right[r_i]
                    r_i += 1
                arr_i += 1
            while l_i < len(left):
                arr[arr_i] = left[l_i]
                l_i += 1
                arr_i += 1
            while r_i < len(right):
                arr[arr_i] = right[r_i]
                r_i += 1
                arr_i += 1

        mergesort(nums, 0, len(nums) - 1)
        return nums