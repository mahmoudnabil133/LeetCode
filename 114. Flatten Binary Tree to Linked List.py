# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.convert(root)
        return root
    def convert(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left = self.convert(root.left)
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None
        right = self.convert(root.right)
        return right


        