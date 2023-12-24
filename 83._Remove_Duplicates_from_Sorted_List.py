# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        values = []
        prev = None
        while head:
            if head.val in values:
                head = head.next
                prev.next = head
            else:
                prev = head
                values.append(head.val)
                head = head.next
        return res


        