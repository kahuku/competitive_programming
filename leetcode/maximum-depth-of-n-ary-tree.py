"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = [(root, 1)]
        deepest = 1
        while q:
            node, level = q.pop(0)
            if not node: continue
            for child in node.children:
                q.append((child, level + 1))
            deepest = max(deepest, level)
        return deepest