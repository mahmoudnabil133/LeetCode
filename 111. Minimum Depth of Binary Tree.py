# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
    def depth(self, root):
        if not root:
            return 0
        lh = self.depth(root.left)
        rh = self.depth(root.right)
        if not lh:
            return rh+1
        if not rh:
            return lh+1 
        return (self.min(lh, rh) + 1)
    def min(self, a,b):
        if a < b:
            return a
        return b
