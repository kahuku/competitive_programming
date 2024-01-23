# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        my_head = ListNode()
        my_node = my_head
        s = 0
        while node:
            if node.val == 0:
                my_node.next = ListNode(s)
                my_node = my_node.next
                s = 0
            else:
                s += node.val
            node = node.next
        return my_head.next