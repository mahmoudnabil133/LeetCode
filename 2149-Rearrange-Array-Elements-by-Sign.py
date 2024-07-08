class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        out = []
        l, r = 0, 0
        n = len(nums)
        while l < n and r< n:
            while l < n and nums[l] < 0:
                l+=1
            if l < n:
                out.append(nums[l])
                l+=1
            while r < n and nums[r] > 0:
                r+=1
            if r < n:
                out.append(nums[r])
                r+=1
        return out