# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        cur1 = head
        cur2 = head
        count = 0

        while cur1:
            count +=1
            cur1 = cur1.next
        
        itirates = count - n -1

        if itirates < 0:
            return head.next

        while itirates:
            cur2 = cur2.next
            itirates -=1
        cur2.next = cur2.next.next
        return head
        