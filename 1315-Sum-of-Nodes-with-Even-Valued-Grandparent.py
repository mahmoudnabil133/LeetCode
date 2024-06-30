# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sum_even(root, lvl, lvls):
            nonlocal tot
            if not root:
                return None
            if lvl in lvls:
                tot += root.val
            if root.val %2 == 0:
                lvls.append(lvl+2)
            sum_even(root.left,lvl+1, lvls)
            sum_even(root.right, lvl+1, lvls)
            
            if root.val %2 == 0:
                lvls.pop()
            return None
        tot = 0
        sum_even(root, 0, [])
        return tot