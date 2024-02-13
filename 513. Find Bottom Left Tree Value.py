"find bottom left val of tree"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
       
        def deeperLeft(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            left = deeperLeft(root.left)
            right = deeperLeft(root.right)
            if left and right:
                if len(left) >= len (right):
                    return left + [root.val]
                else:
                    return right + [root.val]
            elif left and not right:
                return left + [root.val]
            elif  right and not left:
                return right + [root.val]
        paths = deeperLeft(root)
        if not paths:
            return 0
        return paths[0]
        
