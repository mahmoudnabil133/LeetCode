# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        old_head = head
        while head:
            nodes.append(head.val)
            head = head.next
        
        if len(nodes) > 1:
            nodes.sort()
        else:
            return old_head
        new_head = ListNode(nodes[0])
        cur = new_head
        for i in range(1, len(nodes), 1):
            node = ListNode(nodes[i])
            cur.next = node
            cur = node
        return new_head



        