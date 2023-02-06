# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None
        print(original.val)
        if original.val == target.val:
            return cloned
        l = self.getTargetCopy(original.left, cloned.left, target)
        if not l:
            return self.getTargetCopy(original.right, cloned.right, target)
        return l
            