# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if root.val == targetSum:
            return [[root.val]]
        path1 = self.pathSum(root.left, targetSum - root.val)
        path2 = self.pathSum(root.right, targetSum - root.val)
        ret = []
        if path1:
            for path in path1:
                path.insert(0, root.val)
                ret.append(path)
        if path2:
            for path in path2:
                path.insert(0, root.val)
                ret.append(path)
            
        return ret
