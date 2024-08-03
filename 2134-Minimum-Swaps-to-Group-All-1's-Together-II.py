class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = nums.count(1)
        l, r = 0, totalOnes - 1
        windowZeros = nums[:totalOnes].count(0)
        nums+= nums[:totalOnes]
        minSwaps = windowZeros
        while r < len(nums)-1:
            if nums[l] == 0:
                windowZeros -= 1
            l += 1
            r += 1
            if nums[r] == 0:
                windowZeros += 1
            minSwaps = min(minSwaps, windowZeros)
        return minSwaps 
