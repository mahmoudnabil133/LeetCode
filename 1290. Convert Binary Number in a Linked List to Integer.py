# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        mul = 1
        binary = 0
        while num:
            top = num.pop()
            binary += (top * mul)
            mul *= 2
        return binary
        