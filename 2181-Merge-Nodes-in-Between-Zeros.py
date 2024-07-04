# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sumBetZeros = []
        cur = head.next
        sumNodes = 0 
        while cur:
            if cur.val == 0:
                sumBetZeros.append(sumNodes)
                sumNodes = 0
            else:
                sumNodes += cur.val
            cur = cur.next
        past = None
        while sumBetZeros:
            newHead = ListNode(sumBetZeros.pop())
            newHead.next = past
            past = newHead
        return newHead