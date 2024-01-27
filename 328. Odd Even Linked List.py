# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        ev_start = head
        od_start = head.next
        cnt = 0
        while head.next:
            coming = head.next
            head.next = head.next.next
            if cnt % 2 == 0 and head.next:
                final_ev = head.next
            elif  cnt % 2 == 1 and head.next:
                final_od = head.next
            cnt += 1
            head = coming
        final_ev.next = od_start
        return ev_start
