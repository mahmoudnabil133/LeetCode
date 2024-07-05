class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        l, r = 0, len(nums)-1
        avg = float("inf")
        print(nums)
        while l < r:
            avg = min(avg, (nums[l] + nums[r]) /2)
            l+=1
            r-=1
        return avg