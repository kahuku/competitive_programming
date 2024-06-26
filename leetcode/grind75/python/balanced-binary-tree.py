# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time | O(n) space
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if root is None: return True

        l = height(root.left)
        r = height(root.right)
        if max(l, r) - min(l, r) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)