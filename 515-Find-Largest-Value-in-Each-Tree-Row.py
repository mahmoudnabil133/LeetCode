# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        lvl_max_nodes = []
        while q:
            n = len(q)
            max_node = float(\-inf\)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                max_node = max(max_node, node.val)
            lvl_max_nodes.append(max_node)
        return lvl_max_nodes
                
                