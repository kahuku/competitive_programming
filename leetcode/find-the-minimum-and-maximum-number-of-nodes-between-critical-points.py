# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexes = []
        prev = head.val
        next = None
        node = head.next
        i = 1
        while node.next:
            next = node.next.val
            if prev > node.val and node.val < next:
                indexes.append(i)
            if node.val > next and prev < node.val:
                indexes.append(i)
            prev = node.val
            node = node.next
            i += 1
        
        if len(indexes) < 2:
            return [-1, -1]
        else:
            mi, ma = float('inf'), indexes[-1] - indexes[0]
            for i in range(1, len(indexes)):
                mi = min(mi, indexes[i] - indexes[i - 1])
            return [mi, ma]
