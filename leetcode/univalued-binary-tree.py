# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # BFS
        val = root.val
        q = [root]
        while q:
            node = q.pop(0)
            if node.val != val:
                return False
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return True

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def search(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return search(node.left, val) and search(node.right, val)
        return search(root, root.val)