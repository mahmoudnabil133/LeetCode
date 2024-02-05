"how to get k th min value of a tree"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        ret = self.getMin(root)
        ret.sort()
        return ret[k-1]
    def getMin(self,root):
        if not root:
           return []
        out = []
        if not root.left and root.right:
            out = self.getMin(root.right)
        elif not root.right and root.left:
            out = self.getMin(root.left)
        else:
            out = self.getMin(root.left) + self.getMin(root.right)
        return out+[root.val]
        