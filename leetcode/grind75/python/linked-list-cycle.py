# Linked List, set

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time | O(n) space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        curr = head
        s = set()
        while curr.next:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False