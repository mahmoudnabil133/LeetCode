# Definition for singly-linked list.
"return ture if there is a cycle in linked list else return false"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        stack = []
        while head:
            if head.next in stack:
                return True
            stack.append(head)
            head = head.next
        return False
