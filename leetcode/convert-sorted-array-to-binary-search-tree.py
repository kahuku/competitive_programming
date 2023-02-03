# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def setup(arr):
            if not arr or len(arr) == 0:
                return None
            mid = len(arr) // 2
            l = setup(arr[:mid])
            r = setup(arr[mid+1:]) if len(arr) > mid + 1 else None
            return TreeNode(arr[mid], l, r)

        return setup(nums)