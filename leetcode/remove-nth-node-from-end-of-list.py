# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        remove, i, node, d = None, 0, head, {}
        while node:
            d[i] = node
            i += 1
            node = node.next

        if n == 0 or n == i:
            nex = head.next
            head.next = None
            return nex
        
        node = d[i - n - 1]
        node.next = node.next.next if node.next else None
        return head