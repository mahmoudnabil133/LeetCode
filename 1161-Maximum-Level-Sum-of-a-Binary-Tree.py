# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        lvl = 0
        max_lvl = 0
        max_sum = float("-inf")
        while q:
            lvl += 1
            cur_sum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cur_sum += node.val
            
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_lvl = lvl
        return max_lvl
                
