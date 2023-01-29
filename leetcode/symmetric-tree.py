# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def left(node):
            return [node.val] + left(node.left) + left(node.right) if node else [None]
        def right(node):
            return [node.val] + right(node.right) + right(node.left) if node else [None]
        print(left(root.left), right(root.right))
        return left(root.left) == right(root.right) if root else False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(left, right):
            if not left or not right:
                return left is right
            if left.val != right.val:
                return False
            return preorder(left.left, right.right) and preorder(left.right, right.left)
        return not root or preorder(root.left, root.right)