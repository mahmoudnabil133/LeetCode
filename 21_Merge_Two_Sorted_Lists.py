#!/usr/bin/python3
"""
merge 2 sorted linked lists it may have repeated val
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        else:
            head = None
            "define a head of our node" 
            if list1.val <= list2.val:
                head = list1
            else:
                head = list2
            "iterate each of them and merge"
            while list1 and list2:
                while list1.val <= list2.val and list1.next:
                    if list1.next.val > list2.val:
                        break
                    list1 = list1.next
                if list1.val <= list2.val:
                    current = list1
                    list1 = list1.next
                    current.next = list2
                    if not list1:
                        break
                while list2.val <= list1.val and list2.next:
                    if list2.next.val > list1.val:
                        break
                    list2 = list2.next
                if list2.val <= list1.val:
                    current = list2
                    list2 = list2.next
                    current.next = list1
            return head
