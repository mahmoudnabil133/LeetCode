"""
swap each adjecent node and return
head of linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        orgHead = head
        past = None
        while head and head.next:
            nextNode = head.next
            head.next = nextNode.next
            nextNode.next = head
            if not past:
                orgHead = nextNode
            if past:
                past.next = nextNode
            past = head
            head = head.next
        return orgHead 
