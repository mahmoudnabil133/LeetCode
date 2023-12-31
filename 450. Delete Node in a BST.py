# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteNode2(root, key):
            if not root:
                return root
            if (key < root.val):
                root.left = deleteNode2(root.left, key)
            elif(key > root.val):
                root.right = deleteNode2(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    root.val = getMin(root.right)
                    print(root.val)
                    root.right = deleteNode2(root.right, root.val)
            return root
        
        def getMin(root):
            while root.left:
                root = root.left
            return root.val
        
        root = deleteNode2(root, key)
        return root
