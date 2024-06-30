# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, l):
            if not root:
                return None
            dfs(root.left, l)
            l.append(root.val)
            dfs(root.right, l)
        l1 = []
        l2 = []
        dfs(root1, l1)
        dfs(root2, l2)
        l1 += l2
        res = sorted(l1)
        return res