"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None
        row, ans = [], []
        last_level = 0
        q = [(root, last_level)]
        while q:
            node, level = q.pop(0)
            for child in node.children:
                q.append((child, level + 1))
            if level != last_level:
                ans.append(row)
                row = []
                last_level = level
            row.append(node.val)

        ans.append(row)
        return ans