# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        cur = head
        prev = dummy

        while cur:
            if cur.next and cur.val == cur.next.val:
                dupVal = cur.val
                while cur and cur.val == dupVal:
                    #move cur to the next node
                    cur = cur.next
                #after the loop set prev to cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next