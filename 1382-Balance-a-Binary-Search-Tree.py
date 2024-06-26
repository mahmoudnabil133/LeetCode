# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def hieght(root):
            if not root:
                return -1
            return max(hieght(root.left), hieght(root.right))+1
        in_list = []
        def inorder(root, inorder_list):
            if not root:
                return
            inorder(root.left, inorder_list)
            inorder_list.append(root.val)
            inorder(root.right, inorder_list)
        
        def build_balance_tree(inorder, l, r):
            if r < l:
                return None
            mid = (l+r) // 2

            left = build_balance_tree(inorder, l, mid-1)
            right = build_balance_tree(inorder, mid+1, r)

            root = TreeNode(inorder[mid], left, right)
            return root
        inorder(root, in_list)

        return build_balance_tree(in_list, 0, len(in_list)-1)

        