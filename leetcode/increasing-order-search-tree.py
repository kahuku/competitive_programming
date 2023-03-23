# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def search(node, q):
            if node.left: q = search(node.left, q)
            q = q + [node]
            if node.right: q = search(node.right, q)
            node.left = None
            node.right = None
            return q

        q = search(root, [])

        root = q.pop(0)
        node = root
        while q:
            node.left = None
            node.right = q.pop(0)
            node = node.right
        return root