# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(node):
            curr = node
            prev = None
            while curr:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node2 = reverse(slow.next)
        slow.next = None
        node = head
        while node2:
            node2Next = node2.next
            currNext = node.next
            node.next = node2
            node2.next = currNext
            node = currNext
            node2 = node2Next