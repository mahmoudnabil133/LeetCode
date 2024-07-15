# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = None
        dic = {}
        parents = set()
        childs = set()
        for node in descriptions:
            # is parent in created or not
            if dic.get(node[0]):
                parent = dic[node[0]]
            else:
                parent = TreeNode(node[0])
                dic[node[0]] = parent
            parents.add(node[0])
            # is child created or not
            if dic.get(node[1]):
                child = dic[node[1]]
            else:
                child = TreeNode(node[1])
                dic[node[1]] = child
            childs.add(node[1])
            # check if child left or right
            if node[2]:
                parent.left = child
            else:
                parent.right = child
        for p in list(parents):
            if p not in childs:
                root = dic[p]       
        return root