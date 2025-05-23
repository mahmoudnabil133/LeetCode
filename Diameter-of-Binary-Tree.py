# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length, max_diameter = self.getDiameter(root)
        return max(max_length, max_diameter)
    
    def getDiameter(self , root):
        if not root:
            return (-1, -1)
        if not root.left and not root.right:
            return (0, 0)
        
        left_length, left_diameter = self.getDiameter(root.left)
        right_length, right_diameter = self.getDiameter(root.right)

        left_length += 1
        right_length += 1

        return (max(left_length, right_length), max(left_diameter, right_diameter, left_length + right_length))
        