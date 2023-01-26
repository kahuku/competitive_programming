class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = []
        tot = reduce((lambda x, y: x * y), nums)
        if tot == 0:
            zeros = nums.count(0)
            if zeros == 1:
                tot = reduce((lambda x, y: x * y), [num for num in nums if num != 0])
                for num in nums:
                    if num == 0:
                        ans.append(tot)
                    else:
                        ans.append(0)
                return ans
            else:
                return [0 for _ in range(len(nums))]
        else:
            for i in range(len(nums)):
                ans.append(int(tot * nums[i] ** -1))
            return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, operator.mul))
        post = list(accumulate(nums[::-1], operator.mul))[::-1]
        return [(pre[i - 1] if i > 0 else 1) * (post[i + 1] if i < len(nums) - 1 else 1) for i in range(len(nums))]