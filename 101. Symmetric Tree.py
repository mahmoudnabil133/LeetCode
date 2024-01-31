"as a merror we see if tree is symmetreic or not "
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return (self.sameTree(root.left, root.right))
    
    def sameTree(self,l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        if (l.val != r.val):
            return False
        if (l.val == r.val and not r.left and not r.right and not l.left and not l.right):
            return True
        if (self.sameTree(l.left, r.right) and self.sameTree(l.right, r.left)):
            return True
        return False
