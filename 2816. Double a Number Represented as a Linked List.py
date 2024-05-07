# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        car = 0 

        while stack:
            node = stack.pop()
            dub = ( node.val * 2 ) + car
            node_val = dub % 10
            node.val = node_val
            car = ( dub - node_val ) // 10
        if car:
            node = ListNode(car)
            node.next = head
            head = node
        return head
