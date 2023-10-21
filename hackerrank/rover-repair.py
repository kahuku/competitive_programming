from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(l):
    root = TreeNode(l[0])
    q = deque()
    q.append(root)
    i = 1
    while q:
        node = q.popleft()
        if node:
            node.left = TreeNode(l[i]) if i < len(l) else None
            node.right = TreeNode(l[i + 1]) if i + 1 < len(l) else None
            q.append(node.left)
            q.append(node.right)
            i += 2
    return root

def inorder(root):
    path = []
    def recurse(node):
        if node:
            recurse(node.left)
            if node.val != 'empty':
                path.append(node.val)
            recurse(node.right)
    recurse(root)
    return path

def find_swapped_elements(nums):
    first = second = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if first is None:
                first = i
            second = i + 1

    if first is not None:
        return nums[first], nums[second]
    else:
        return nums[0], nums[-1]

l = [input() for _ in range(int(input()))]
root = list_to_tree(l)
path = inorder(root)
a, b = find_swapped_elements([int(i) for i in path])
print(f"Swap nodes {min(a, b)} and {max(a, b)}")