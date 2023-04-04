class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr, low, high):
            if low < high:
                mid = (high - low) // 2 + low
                mergesort(arr, low, mid)
                mergesort(arr, mid + 1, high)
                merge(arr, low, mid, high)
        
        def merge(arr, l, mid, r):
            left = arr[l:mid+1]
            right = arr[mid+1:r+1]
            i, j, arr_i = 0, 0, l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[arr_i] = left[i]
                    i += 1
                else:
                    arr[arr_i] = right[j]
                    j += 1
                arr_i += 1
            while i < len(left):
                arr[arr_i] = left[i]
                i += 1
                arr_i += 1
            while j < len(right):
                arr[arr_i] = right[j]
                j += 1
                arr_i += 1
        
        mergesort(nums, 0, len(nums) - 1)
        return nums