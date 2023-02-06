# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.s = 0
        def search(node, left):
            if not node.left and not node.right and left:
                self.s += node.val
            if node.left:
                search(node.left, True)
            if node.right:
                search(node.right, False)

        search(root, False)
        return self.s