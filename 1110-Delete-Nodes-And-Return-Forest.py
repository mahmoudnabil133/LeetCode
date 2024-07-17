# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return None
        q = deque()
        trees = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            trees.append(root)
        else:
            root.val = 0
        q.append(root)

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    if node.left.val in to_delete:
                        node.left.val = 0
                    q.append(node.left)
                    if node.left.val == 0:
                        node.left = None
                if node.right:
                    if node.right.val in to_delete:
                        node.right.val = 0
                    q.append(node.right)
                    if node.right.val == 0:
                        node.right = None
                if node.val == 0:
                    if node.left:
                        if node.left.val:
                            trees.append(node.left)
                    if node.right:
                        if node.right.val:
                            trees.append(node.right)
        return trees