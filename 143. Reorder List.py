"""
reorder linked list in a way
one of front one of end and so on
i solved it recursevly
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        "give head and and current to reorder function"
        self.reorder(head, head)
        return head
    def reorder(self, current, head):
        "last node of list: ret it to the prev node"
        if not current.next:
            return current, head
        node, head = self.reorder(current.next, head)
        if not node or not head:
            return None, None
        "prev node link the returned node to head and change head"
        node.next = head.next
        head.next = node
        head = node.next
        "cut list wich you linked to head"
        current.next = None
        "case we finish linking and want to stop linking so return None"
        if head == current or head.next == current:
            return None, None
        "return current and updated head"
        return current, head
