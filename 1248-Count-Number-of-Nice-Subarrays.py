class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        cur_odd = 0
        cur_sub = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                cur_odd +=1
                cur_sub = 0
            while cur_odd == k:
                if nums[l] % 2:
                    cur_odd -=1
                l +=1
                cur_sub += 1
            
            # works when nums[r] is even or odd
            # this works as we add the other sub arraies if we put the
            # left pointer to index 0 again
            ans += cur_sub
        return ans