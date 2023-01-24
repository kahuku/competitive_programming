# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast, slow = head.next, head
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        node = head
        while node is not None:
            if node not in s:
                s.add(node)
            else:
                return True
            node = node.next
        return False