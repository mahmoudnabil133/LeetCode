# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root, nums):
            if not root:
                return None
            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)
        nums = []
        inorder(root, nums)
        l, r = 0, len(nums) -1 

        while l != r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] < k:
                l +=1
            elif nums[l] + nums[r] > k:
                r -= 1
        return False
