# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        def convert(listNodes, l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2

            leftSub = convert(listNodes, l, mid-1)
            rightSub = convert(listNodes, mid+1, r)
            
            return TreeNode(listNodes[mid], leftSub, rightSub)
        return convert(nodes, 0, len(nodes) - 1)
        