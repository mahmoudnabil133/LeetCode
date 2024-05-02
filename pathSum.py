# again path sum to review recursion and backtracking problems.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        paths = self.helper(root, targetSum)
        print(paths)
        for path in paths:
            if sum(path) == targetSum:
                return True
        return False
    def helper(self, root, targetSum):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        left , right= self.helper(root.left, targetSum), self.helper(root.right, targetSum)
        for l in left :
            l.append(root.val)
        for x in right:
            x.append(root.val)
    
        return (left + right)
