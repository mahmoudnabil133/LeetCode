"move zeros to end"
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        while j < len(nums):
            if i < len(nums):
                if nums[i] != 0:
                    nums[j] = nums[i]
                    j += 1
            else:
                nums[j] = 0
                j += 1
            i += 1
