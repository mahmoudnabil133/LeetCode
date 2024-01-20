# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l1 = []
        l2 = self.post(root, l1)
        return l2
    def post(self, root, list1):
        if not root:
            return list1
        self.post(root.left, list1)
        self.post(root.right, list1)
        list1.append(root.val)
        return list1
