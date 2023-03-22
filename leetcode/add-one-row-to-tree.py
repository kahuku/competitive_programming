# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        q = [root]
        d = 2
        while q:
            if d == depth:
                while q:
                    node = q.pop(0)
                    left, right = node.left, node.right
                    new_left, new_right = TreeNode(val), TreeNode(val)
                    node.left = new_left
                    new_left.left = left
                    node.right = new_right
                    new_right.right = right
            else:
                q_len = len(q)
                for i in range(q_len):
                    node = q.pop(0)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            d += 1
        
        return root