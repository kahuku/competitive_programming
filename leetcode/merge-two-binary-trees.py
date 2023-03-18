# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        if not root1: return root2
        if not root2: return root1

        new_root = TreeNode()
        q = [(root1, root2, new_root)]
        while q:
            node1, node2, new_node = q.pop(0)

            if node1 and node2:
                new_node.val += node1.val
                new_node.val += node2.val
                if node1.left or node2.left: 
                    new_node.left = TreeNode()
                    q.append((node1.left, node2.left, new_node.left))
                if node1.right or node2.right: 
                    new_node.right = TreeNode()
                    q.append((node1.right, node2.right, new_node.right))
            elif node1:
                new_node.val += node1.val
                if node1.left:
                    new_node.left = TreeNode()
                    q.append((node1.left, None, new_node.left))
                if node1.right:
                    new_node.right = TreeNode()
                    q.append((node1.right, None, new_node.right))
            elif node2:
                new_node.val += node2.val
                if node2.left:
                    new_node.left = TreeNode()
                    q.append((None, node2.left, new_node.left))
                if node2.right:
                    new_node.right = TreeNode()
                    q.append((None, node2.right, new_node.right))

        return new_root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        if root1 and root2:
            new_root = TreeNode(root1.val + root2.val)
            new_root.left = self.mergeTrees(root1.left, root2.left)
            new_root.right = self.mergeTrees(root1.right, root2.right)
            return new_root
        return root1 if root1 else root2