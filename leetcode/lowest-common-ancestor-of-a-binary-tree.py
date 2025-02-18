# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [p, q, None]: return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
    

        # Equivalent return statements:

        # a
        # return root if l and r else l if l else r

        # b
        return root if l and r else l or r
        
        # c
        # if l and r:
        #     return root
        # return [l, r][l == None]

        # d
        # return next((x for x in (root, l, r) if x is not None))