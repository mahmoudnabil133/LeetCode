"return connected nodes in linked list and in nums array"
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        conn = 0
        while head:
            if head.val not in nums:
                head = head.next
            else:
                while head and head.val in nums:
                    head = head.next
                conn += 1 
        return conn
