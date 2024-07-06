# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        lvl = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
            l, r = 0, len(q) - 1
            
            if lvl % 2 == 1:
                while l < r:
                    left = q[l]
                    right = q[r]
                    left.val, right.val = right.val, left.val
                    l += 1
                    r -= 1
        return root 
