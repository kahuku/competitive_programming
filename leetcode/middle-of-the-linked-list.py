# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_nodes = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            num_nodes += 1

        print(num_nodes)

        i = num_nodes // 2
        curr = head
        for _ in range(i):
            curr = curr.next
        
        return curr