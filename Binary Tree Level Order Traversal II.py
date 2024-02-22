# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            lvl = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                value = node.val
                lvl.append(value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl)
        res.reverse()
        return res
