"get max path sum"
"""
how to solve
1) at each node get serculer gain - compare - update maxGain)
2) at each node return maxPath left or right so you can add values to it at parent node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxGain = float('-inf')
        def getMax(root):
            nonlocal maxGain
            if not root:
                return 0
            leftGain = max(getMax(root.left), 0)
            rightGain = max(getMax(root.right), 0)
            currentMax = leftGain + root.val + rightGain
            maxGain = max(currentMax, maxGain)

            return root.val + max(leftGain, rightGain)
        getMax(root)
        return maxGain
