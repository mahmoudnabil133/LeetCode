"remove middle of linked list if num of nodes is n then mid index = (n // 2)"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        cur = head
        nodes = 0
        while cur:
            nodes += 1
            cur = cur.next
        itr = (nodes // 2) - 1
        cur2 = head
        while itr:
            cur2 = cur2.next
            itr -= 1
        cur2.next = cur2.next.next
        return head
