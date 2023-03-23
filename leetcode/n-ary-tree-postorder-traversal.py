"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def search(node, l):
            for child in node.children:
                l = search(child, l)
            l.append(node.val)
            return l

        return search(root, []) if root else []