# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        solution = [[root.val]]
        nodes_list = [[root]]
        while len(nodes_list) > 0:
            nodes = nodes_list.pop(0)
            levelNodes = []
            levelSolution = []
            while len(nodes) > 0:
                node = nodes.pop(0)
                if node.left:
                    levelNodes.append(node.left) 
                    levelSolution.append(node.left.val)
                if node.right:
                    levelNodes.append(node.right)
                    levelSolution.append(node.right.val)
            if len(levelNodes) > 0:
                nodes_list.append(levelNodes)
                solution.append(levelSolution)

        return solution