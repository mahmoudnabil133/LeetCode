# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        "iterate the paths and return sumPaths"
        retList = self.getList(root)
        sumPaths = 0
        for path in retList:
            mul = 1
            for val in path:
                sumPaths += (val * mul)
                mul *= 10
        return sumPaths
    def getList(self, root):
        "when root is None"
        if not root:
            return []
        "when root is leaf node"
        if not root.left and not root.right:
            return [[root.val]]
        """
        when root is parent return 2d arr with left and
        right paths then append current val to end of each path
        """
        leftList = self.getList(root.left)
        rightList = self.getList(root.right)
        leftList += rightList.copy()
        ret = leftList.copy()
        for l in ret:
            l.append(root.val)
        "finally return all posiple paths as 2d arr to main function"
        return ret
