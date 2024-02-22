# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root.left and not root.right:
            return [root.val]
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            lvl = []
            for i in range(qlen):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sumlvl = 0
            for i in lvl:
                sumlvl += i
            sumlvl /= len(lvl)
            res.append(sumlvl)
        return res
