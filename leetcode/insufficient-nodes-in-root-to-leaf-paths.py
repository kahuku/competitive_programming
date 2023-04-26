# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def search(node, val):
            if not node:
                return False
            val += node.val
            if not node.left and not node.right:
                node.valid = (val >= limit)
            else:
                l, r = search(node.left, val), search(node.right, val)
                node.valid = l or r

            print(node.val, node.valid)
            return node.valid

        def build(old, new):
            if old.left and old.left.valid:
                new.left = TreeNode(old.left.val)
                build(old.left, new.left)
            if old.right and old.right.valid:
                new.right = TreeNode(old.right.val)
                build(old.right, new.right)
        
        search(root, 0)

        if not root.valid: return None

        newRoot = TreeNode(root.val)
        build(root, newRoot)

        return newRoot