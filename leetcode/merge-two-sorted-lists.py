# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        if l1 != None and l2 != None:
            if l1.val <= l2.val:
                head = ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next
        elif l1 == None:
            return l2
        else:
            return l1
        
        curr = head
        while l1 != None or l2 != None:
            if l1 == None:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            elif l2 == None:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    curr.next = ListNode(l1.val)
                    curr = curr.next
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    curr = curr.next
                    l2 = l2.next

        return head