class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)-2):
            one = i
            j = i + 1
            found_j, found_k = False, False
            while j < len(nums) - 1:
                if nums[j] - nums[i] == diff:
                    found_j = True
                    break
                j += 1
            if not found_j:
                continue
            k = j + 1
            while k < len(nums):
                if nums[k] - nums[j] == diff:
                    found_k = True
                    break
                k +=1  
            if not found_k:
                continue
            else:
                print(nums[i], nums[j], nums[k])
                count +=1
        return count
                