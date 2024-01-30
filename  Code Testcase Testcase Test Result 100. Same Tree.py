"""
geven 2 trees 
required:
check if 2 are same or not 
with traversing and recursion it is solved
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val == q.val and p.left== None and p.right == None and q.left == None and q.right == None:
            return True
        if p.val == q.val:
            if (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):
                return True
        return False
