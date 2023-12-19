# totally wrong logic

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        num = root.val
        left = self.longestUnivaluePath(root.left)
        right = self.longestUnivaluePath(root.right)

        lv, rv = float('inf'), float('inf')
        if root.left:
            lv = root.left.val
        if root.right:
            rv = root.right.val
        
        if num == lv == rv:
            return 2 + left + right
        elif num == lv:
            return 1 + left
        elif num == rv:
            return 1 + right
        return max(left, right)