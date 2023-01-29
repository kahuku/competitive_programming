# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        node = root
        direction = None
        while node:
            print(node.val)
            if node.val > val:
                direction = 'l'
                new_node = node.left
            else:
                direction = 'r'
                new_node = node.right
            if new_node is None:
                print('adding node')
                if direction == 'l':
                    node.left = TreeNode(val)
                else:
                    node.right = TreeNode(val)
                break
            else:
                node = new_node

        return root