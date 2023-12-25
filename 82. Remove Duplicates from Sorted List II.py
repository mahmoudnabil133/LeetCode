# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        res = head
        values = []
        dub = []
        prev = None
        while head:
            if head.val in values:
                prev.next = head.next
                dub.append(head.val)
                head = head.next
         
            else:
                prev = head
                values.append(head.val)
                head = head.next
        
        cur = res
        prev = None
        
        while cur:
            if cur.val in dub:
                if prev ==None:
                    cur = cur.next
                    res = cur
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return res
