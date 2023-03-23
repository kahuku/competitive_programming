"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def search(node, l):
            l.append(node.val)
            for child in node.children:
                l = search(child, l)
            return l
        return search(root, []) if root else []