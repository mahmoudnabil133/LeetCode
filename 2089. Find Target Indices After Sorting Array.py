class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ls = []
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid-1
            else:
                go_right = mid
                while mid > 0 and nums[mid-1] == target:
                    mid-=1
                left = mid

                while go_right < len(nums)-1 and nums[go_right + 1] == target:
                    go_right += 1
                right = go_right
                return [i for i in range(left, right+1, 1)]
        return []        
            
