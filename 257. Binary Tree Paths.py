"""
(257. Binary Tree Paths) 
(Easy level)
but i think its not easy at all see and decside
gevin: a tree root
wanted :return list of paths of this tree

steps of solution:

1) iterate tree recursevly
2) get left paths in 2d arr
3) get righ paths in 2d arr
4) append value of current root to each path of left&right paths
5) merge left and right paths
6) return merged list
8) in binaryTreePaths function do:
    a) itr each list of lists and convrt it to wanted string
        like 1->2->3
    b) append str list to strPaths arr
    c) return strPaths arr
now we solved problem and finally still the code implimentation lets code it.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        lists = self.getPaths(root)
        strPath = []
        "itr returned lists and convert them to wanted str"
        for path in lists:
            head = str(path.pop())
            while path:
                head += '->'
                head += str(path.pop())
            "append each path (head) to str path"
            strPath.append(head)
        "return str paths in 2 dimentional arr"
        return strPath

    def getPaths(self, root):
        if not root:
            return []
        "if root is leaf node return its val"
        if not root.left and not root.right:
            return [[root.val]]
        "if not leaf node do recursion in left and right subtrees"
        left = self.getPaths(root.left)
        right = self.getPaths(root.right)
        "now we got left and right"
        "append value of current root to each lsit of left paths"
        if left:
            for l in left:
                l.append(root.val)
        "append value of current root to each list of right paths"
        if right:
            for l in right:
                l.append(root.val)
        "merge 2 lists left and right then return"
        tot = left + right
        return tot
        