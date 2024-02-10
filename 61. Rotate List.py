"rotate list k time"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        "ret head if head is none or contain 1 node (you will not rot 1 node)"
        if not head or not head.next:
            return head
        current = head
        "calc sum of nodes in list"
        sumNodes = 0
        while current:
            sumNodes += 1
            if not current.next:
                break
            current = current.next
        "if you rot list with k = sumNodes time no change to our list"
        "so calc real times we will rot"
        loops = k % sumNodes
        if loops == 0:
            return head
        rot = sumNodes - loops -1
        "itr list again to git new head and cut the list till out new head"
        cur2 = head
        while rot:
            cur2 = cur2.next
            rot-=1
        current.next = head
        newHead = cur2.next
        cur2.next = None
        "ret new head"
        return newHead

        
