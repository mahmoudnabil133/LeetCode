# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1 = []
        l2 = self.pre(root, l1)
        return l2
    def pre(self, root, list1):
        if not root:
            return list1
        list1.append(root.val)
        self.pre(root.left, list1)
        self.pre(root.right, list1)
        return list1
