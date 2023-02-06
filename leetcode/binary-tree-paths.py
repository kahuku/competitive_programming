# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        paths = []

        def search(node, path):
            path = path + str(node.val) + "->"
            if not node.left and not node.right:
                paths.append(path[:-2])
            if node.left:
                search(node.left, path)
            if node.right:
                search(node.right, path)

        search(root, '')
        return paths