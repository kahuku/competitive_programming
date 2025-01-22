# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preorder = []

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: return None

        if preorder is not None: self.preorder = preorder

        root = self.preorder[0] ####
        self.preorder = self.preorder[1:]

        i = inorder.index(root)
        lc = inorder[:i]
        rc = inorder[i+1:] if i != len(inorder) - 1 else []

        root = TreeNode(root)
        root.left = self.buildTree(None, lc)
        root.right = self.buildTree(None, rc)

        return root