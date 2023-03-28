# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def search(node, path):
            if not node.left and not node.right:
                path.append(str(node.val))
                self.ans += int(''.join(path))
                return
            if node.left:
                search(node.left, path + [str(node.val)])
            if node.right:
                search(node.right, path + [str(node.val)])

        search(root, [])
        return self.ans