# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        new_head = ListNode()
        new_head.next = head
        node = head
        prev = new_head
        while node is not None:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return new_head.next