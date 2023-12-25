# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return None
        
        itr = head

        while itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return head
            
        