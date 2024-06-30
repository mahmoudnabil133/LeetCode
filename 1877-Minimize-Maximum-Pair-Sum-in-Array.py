class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        n = len(nums)
        for i in range(n):
            maxSum = max(maxSum, nums[i] + nums[n-1-i])
        return maxSum