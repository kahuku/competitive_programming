# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        row, ans = [], []
        last_level = 0
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
            if level != last_level:
                ans.append(row)
                row = []
                last_level = level
            row.append(node.val)
        ans.append(row)
        return ans[::-1]