# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next:
            return head.val
        nodes = []
        "append values of list to nodes list"
        while head:
            nodes.append(head.val)
            head = head.next
        maxSum = 0
        "get max sum"
        for i in range(len(nodes)):
            if i == len(nodes) // 2:
                break
            sumTwins = nodes[i] + nodes[-1-i]
            if sumTwins > maxSum:
                maxSum = sumTwins
        "return maxSum of twins"
        return maxSum
            