"merge nodes bet zeros"
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
        "iterate the geven list"
        while cur:
            "if cur node is 0 you append calculated sum to outList then assgin sumNode to 0"
            if cur.val == 0:
                sumBetZeros.append(sumNodes)
                sumNodes = 0
            else:
                "update sum"
                sumNodes += cur.val
            cur = cur.next
        past = None
        "convert list to linked list"
        while sumBetZeros:
            newHead = ListNode(sumBetZeros.pop())
            newHead.next = past
            past = newHead
        return newHead
