# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(node):
            if node is None:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        order = inOrder(root)
        return order == sorted(order) and len(set(order)) == len(order)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=-inf, high=inf) -> bool:
        return not root or low < root.val < high and self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)