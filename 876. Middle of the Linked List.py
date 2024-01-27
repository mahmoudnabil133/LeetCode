# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = 0
        cur = head
        while head:
            head = head.next
            nodes += 1
        mid = nodes // 2
        while mid:
            cur = cur.next
            mid -= 1
        return cur
