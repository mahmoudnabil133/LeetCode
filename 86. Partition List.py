"""
split a linked list to
left side: with values less than x
righ side: with values greather than x
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        "head is ptr to None or ptr to list of 1 value"
        if not head or not head.next:
            return head
        """
        create 2 stacks st1 contain ptrs to nodes with less values than x
        and st2 contain ptrs to nodes with values greater than x
        """
        st1 = []
        st2 = []
        curr = head
        "itr list and append to 2 stacks"
        while curr:
            if curr.val < x:
                st1.append(curr)
            else:
                st2.append(curr)
            curr = curr.next
        "pop st2 then st1 and finally return head of list wich will be (past)"
        past = None
        while st2:
            greater = st2.pop()
            greater.next = past
            past = greater
        while st1:
            less = st1.pop()
            less.next = past
            past = less
        return past 
