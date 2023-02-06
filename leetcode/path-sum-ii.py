# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []

        def search(node, path):
            path.append(node.val)
            if node.left is None and node.right is None and sum(path) == targetSum:
                out.append(path)
            if node.left:
                search(node.left, path.copy())
            if node.right:
                search(node.right, path.copy())
        
        if root is not None:
            search(root, [])
        return out
            