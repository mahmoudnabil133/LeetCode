# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(root, maxParent):
            if not root:
                return 0
            good = 0
            if root.val >= maxParent:
                good = 1
            
            left = countGood(root.left, max(maxParent, root.val))
            right = countGood(root.right, max(maxParent, root.val))

            return left + right + good
        return countGood(root, float("-inf"))
            