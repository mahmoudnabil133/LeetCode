# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = dfs(root.left)
            right = dfs(root.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        res+=1
            ret = left + right
            out = []
            for i in ret:
                if i+1 < distance:
                    out.append(i+1)
            return out

        res = 0
        dfs(root)
        return res
