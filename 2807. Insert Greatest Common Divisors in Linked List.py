"""
(Miduim Level)
insert a greatest common factor
inside each 2 elements
---sol--
for each 2 adjesent node
n1 = node1.val
n2 = node2.val
update the factor
wich make mod % to n1 and n2 = 0
till you get the greatest factor
then ins it between 2 nodes
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ret = head
        while head.next:
            n1 = head.val
            n2 = head.next.val
            itr = 1
            while itr <= n1 and itr <= n2:
                if n1 % itr == 0 and n2 % itr == 0:
                    factor = itr
                itr += 1
            ins = ListNode(factor)
            coming = head.next
            head.next = ins
            ins.next = coming
            head = coming
        return ret
