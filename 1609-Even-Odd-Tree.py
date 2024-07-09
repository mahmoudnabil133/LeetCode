# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        lvl = -1
        while q:
            n = len(q)
            cur_lvl_nodes = []
            lvl += 1

            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cur_lvl_nodes.append(node.val)
            #even lvl
            if lvl %2 == 0:
                if cur_lvl_nodes[0] %2 == 0:
                    return False
                for i in range(1, len(cur_lvl_nodes)):
                    if cur_lvl_nodes[i] <= cur_lvl_nodes[i-1]:
                        return False
                    if cur_lvl_nodes[i] %2 == 0:
                        return False
                for n in cur_lvl_nodes:
                    if n %2 == 0:
                        return False
            else:
                if cur_lvl_nodes[0] %2 == 1:
                        return False
                for i in range(1, len(cur_lvl_nodes)):
                    if cur_lvl_nodes[i] >= cur_lvl_nodes[i-1]:
                        return False
                    if cur_lvl_nodes[i] %2 == 1:
                        return False
        return True
