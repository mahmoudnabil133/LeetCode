"number of operations to find sum of k in the list"
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0
        while i < j:
            out = nums[i] + nums[j]
            if out == k:
                i +=1
                j-=1
                cnt += 1
            elif out < k:
                i+=1
            else:
                j-=1
        return cnt
