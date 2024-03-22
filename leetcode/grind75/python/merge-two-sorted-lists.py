# Linked List

class Solution:
    # O(m + n) time | O(1) space
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newcurr, curr1, curr2 = ListNode(), list1, list2
        newhead = newcurr
        while curr1 or curr2:
            if curr1 and curr2 and curr1.val > curr2.val or not curr1 and curr2:
                newcurr.next = curr2
                curr2 = curr2.next
            else:
                newcurr.next = curr1
                curr1 = curr1.next
            newcurr = newcurr.next
        return newhead.next