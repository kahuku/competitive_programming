# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 or not head.next:
            return head
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        k %= n
        if k == 0:
            return head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head