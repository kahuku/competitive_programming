from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            d[level] += node.val
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
        return max(d.items(), key=operator.itemgetter(0))[1]