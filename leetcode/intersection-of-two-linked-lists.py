# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        node = headA
        while node:
            a.append(node)
            node = node.next
        b = []
        node = headB
        while node:
            b.append(node)
            node = node.next
        for node in a:
            if node in b:
                return node