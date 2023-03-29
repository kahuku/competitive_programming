# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node, num, out):
            if node.val >= num:
                out += 1
            if node.left:
                out = search(node.left, max(node.val, num), out)
            if node.right:
                out = search(node.right, max(node.val, num), out)
            return out
        
        return search(root, float("-inf"), 0)