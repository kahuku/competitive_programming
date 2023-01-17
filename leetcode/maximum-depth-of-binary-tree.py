# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(node, depth):
            if node.left and not node.right:
                depth += search(node.left, depth)
            elif not node.left and node.right:
                depth += search(node.right, depth)
            elif node.left and node.right:
                depth += max(search(node.left, depth), search(node.right, depth))
            return depth
        
        return search(root, 1) if root else 0