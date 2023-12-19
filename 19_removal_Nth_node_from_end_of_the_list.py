#!/usr/bin/python3
"""
linked list problem (Medium level)
remove the nth element from the end of the list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        num_of_elements = 0
        while current != None:
            num_of_elements += 1
            current = current.next
        
        iterator = head
        if num_of_elements == n:
            return head.next
        "we minus (1) here to stop before the node we want to remove"
        loops = num_of_elements - n - 1

        while loops:
            iterator = iterator.next
            loops -= 1
        
        iterator.next = iterator.next.next
        return head
        

        