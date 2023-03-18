# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(l):
    """Converts a list to a linked list."""
    head = ListNode()
    curr = head
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    return head.next

def linked_list_to_list(head):
    """Converts a linked list to a list."""
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l

def tree_to_list(root):
    """Converts a binary tree to a list."""
    if not root:
        return []
    l = []
    q = [root]
    while q:
        curr = q.pop(0)
        if curr:
            l.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        else:
            l.append(None)
    return l

def list_to_tree(l):
    """Converts a list to a binary tree."""
    if not l:
        return None
    root = TreeNode(l[0])
    q = [root]
    i = 1
    while q:
        curr = q.pop(0)
        if curr:
            curr.left = TreeNode(l[i]) if i < len(l) else None
            curr.right = TreeNode(l[i+1]) if i+1 < len(l) else None
            q.append(curr.left)
            q.append(curr.right)
            i += 2
    return root

def print_tree(root):
    """Prints a binary tree."""
    if not root:
        return
    q = [root]
    while q:
        curr = q.pop(0)
        if curr:
            print(curr.val, end=' ')
            q.append(curr.left)
            q.append(curr.right)
        else:
            print('null', end=' ')
    print()

def print_linked_list(head):
    """Prints a linked list."""
    while head:
        print(head.val, end=' ')
        head = head.next
    print()
