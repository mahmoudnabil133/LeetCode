# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def postOrder(root, parentSum):
            if not root:
                return 0
            right = postOrder(root.right, parentSum)
            if not right:
                root.val += parentSum
            else:
                root.val+= right
            left = postOrder(root.left, root.val)
            if left:
                return left
            return root.val
        postOrder(root, 0)
        return root