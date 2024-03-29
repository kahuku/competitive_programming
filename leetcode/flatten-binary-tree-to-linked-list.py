# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None or root.left is None and root.right is None:
            return
        right = root.right
        left = root.left
        root.left = None
        self.flatten(left)
        root.right = left
        self.flatten(right)
        node = root
        while node.right:
            node = node.right
        node.right = right