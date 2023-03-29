# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(arr):
            if not arr: return None
            ma = max(arr)
            m_ind = arr.index(ma)
            node = TreeNode(ma)
            node.left = build(arr[:m_ind])
            node.right = build(arr[m_ind + 1:])
            return node

        return build(nums)