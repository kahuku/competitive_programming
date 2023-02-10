class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        s = set()
        n = len(nums) - 1
        for i in range(n):
            j = i + 1
            k = n
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif tot > target:
                    k -= 1
                else:
                    j += 1
        return [list(triplet) for triplet in s]