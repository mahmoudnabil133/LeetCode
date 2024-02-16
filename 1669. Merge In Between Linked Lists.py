# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = list2
        while list2.next:
            list2 = list2.next
        tail2 = list2
        head1 = list1

        ptr1, ptr2 = None, None
        cnt = 0
        while list1:
            if cnt == a-1:
                ptr1 = list1
            if cnt == b:
                ptr2 = list1.next
                break
            cnt +=1
            list1 = list1.next
        if not ptr1:
            head1 = head2
        else:
            ptr1.next = head2
        tail2.next = ptr2

        return head1
