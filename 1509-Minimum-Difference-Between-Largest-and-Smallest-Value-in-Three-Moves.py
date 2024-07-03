class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()

        minDiff = float("inf")

        for i in range(4):
            left = 3-i
            right = len(nums)- 1 - i
            minDiff = min(minDiff, nums[right] - nums[left])
        
        return minDiff