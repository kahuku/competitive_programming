# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        hl, hr = 0, 0
        l, r = root, root
        while l: hl += 1; l = l.left
        while r: hr += 1; r = r.right
        if hl == hr: return 2 ** hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)