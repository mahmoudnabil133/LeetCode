"""
Reverse a linked list from left var (gevin)
to right var(gevin)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        ret if no linked list or ll have one node or left
        equals right then no reverse(as you rev from node to the same node)
        """
        if not head or not head.next or left == right:
            return head
        newHead  = head
        cur = 1
        "beforeStart won't change if left equals 1"
        beforeStart = None
        """
        itr list and get start node and node before it
        also get end node and node after it so you have 4 nodes
        that allow you reverse the list from each node th other node.
        """
        while cur <= right:
            if cur == left -1:
                beforeStart = head
            elif cur == left:
                start = head
            elif cur == right:
                end = head
            head = head.next
            cur += 1
        afterEnd = head
        "if you want to reverse from start node to other one. then the end node will be our new head"
        if left == 1:
            newHead  = end
        past = afterEnd
        next = None
        while start != afterEnd:
            next = start.next
            start.next = past
            past = start
            start = next
        "in case you dont reverse from start node(given head)"
        if beforeStart:
            beforeStart.next = past
        return newHead 
