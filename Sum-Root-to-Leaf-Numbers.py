# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = self.getPaths(root)
        tot = 0
        for path in paths:
            tot += sum(path)
        return tot

    def getPaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        l_paths = self.getPaths(root.left)
        r_paths = self.getPaths(root.right)

        l_paths += r_paths.copy()

        for l in l_paths:
            l.append(root.val * (10 ** len(l)))
        
        return l_paths
