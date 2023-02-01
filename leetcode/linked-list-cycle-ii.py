# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        i = 0
        node = head
        visited = {}
        while node.next:
            if node in visited.keys():
                return node
            visited[node] = i
            i += 1
            node = node.next
        return None