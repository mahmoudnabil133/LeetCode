"""
medium level
chek if tree is a binary search tree or not
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.check(root) == -1:
            return False
        return True
    def check(self, root):
        if not root:
            return []
        left = self.check(root.left)
        right = self.check(root.right)
        "if node is leaf node return value of node"
        if not left and not right:
            return [root.val]
        """
        if there is error in down trees so return -1 
        as an indication that the down subtree cant be 
        binary search tree 
        """
        if left == -1 or right == -1:
            return -1
        """
        check if value of current node
        is greater then all left values
        and less than all right values
        """
        if left:
            for val in left:
                if root.val <= val:
                    return -1
        if right:
            for val in right:
                if root.val >= val:
                    return -1
        """
        if down trees is perfect then merge left tree values
        and right tree values then append current root and return
        """
        return left + right + [root.val]

        