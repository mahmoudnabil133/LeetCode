# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root, l, h):
            nonlocal Sum
            if not root:
                return
            if root.val <= h and root.val>= l:
                Sum += root.val
            dfs(root.left, l, h)
            dfs(root.right, l, h)
        Sum = 0
        dfs(root, low, high)
        return Sum

            