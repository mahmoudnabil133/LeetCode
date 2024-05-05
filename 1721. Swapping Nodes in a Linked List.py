# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first one is better than second one as it  iterate the list o(n) and the second iterate list o (2 * n)
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        node1 = stack[k-1]
        node2 = stack[len(stack) - k]
        swap = node1.val
        node1.val = node2.val
        node2.val = swap
        return head

        # nodes= 0
        # cur = head
        # while cur:
        #     nodes += 1
        #     cur = cur.next
        # cur2 = head
        # itr = 0
        # ptr1, ptr2 = None, None
        # while cur2:
        #     itr += 1
        #     if itr == k:
        #         ptr1 = cur2
        #     elif itr == (nodes - k + 1):
        #         ptr2 = cur2
            
        #     if ptr1 and ptr2:
        #         swap = ptr1.val
        #         ptr1.val = ptr2.val
        #         ptr2.val = swap
        #         break
        #     cur2 = cur2.next
        # return head

            