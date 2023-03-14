"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        q = [(root, 0)]
        while q:
            node, level = q.pop(0)
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
            next_node, next_level = q[0] if q else (None, -1)
            node.next = next_node if next_level == level else None
        return root