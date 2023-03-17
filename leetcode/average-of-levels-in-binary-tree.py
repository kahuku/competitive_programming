# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [(root, 0)]
        ans = []
        level_sum = 0
        level_count = 0
        last_level = 0
        while q:
            node, level = q.pop(0)
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
            if level == last_level:
                level_sum += node.val
                level_count += 1
            else:
                ans.append(level_sum / level_count)
                level_sum = node.val
                level_count = 1
                last_level = level
        
        return ans + [level_sum / level_count]