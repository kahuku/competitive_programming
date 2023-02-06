# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0
        if not root:
            return 0
        
        def search(node):
            if low <= node.val <= high:
                self.s += node.val
            if node.left:
                search(node.left)
            if node.right:
                search(node.right)

        search(root)
        return self.s