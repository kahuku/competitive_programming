class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # build pre
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(nums[i] + pre[i - 1])

        # build post
        post = [[0] for _ in range(len(nums))]
        post[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] + nums[i]

        # build ans
        ans = []
        for i in range(len(nums)):
            left_count = i
            right_count = len(nums) - i - 1
            l_sum = abs(pre[i-1] - nums[i] * left_count if i else 0)
            r_sum = abs(post[i+1] - nums[i] * right_count if i != len(nums) - 1 else 0)
            ans.append(l_sum + r_sum)
        return ans