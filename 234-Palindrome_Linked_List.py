# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        output = []
        while head:
            output.append(head.val)
            head = head.next
        x = output.copy()
        output.reverse()
        if x == output:
            return True
        return False
            
        