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
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, mi, ma):
            if root is None:
                return True
            
            if root.val <= mi or root.val >= ma:
                return False

            if root.left is not None:
                if root.left.val >= root.val: return False
                lv = helper(root.left, mi, root.val)
                if lv == False: return False
            
            if root.right is not None:
                if root.right.val <= root.val: return False
                rv = helper(root.right, root.val, ma)
                if rv == False: return False
            
            return True

        return helper(root, -float("inf"), float("inf"))