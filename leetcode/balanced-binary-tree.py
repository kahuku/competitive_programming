# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            else:
                return 1 + max(height(node.left), height(node.right))
        
        if root is None:
            return True
        elif height(root.left) > height(root.right) + 1 or height(root.right) > height(root.left) + 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        