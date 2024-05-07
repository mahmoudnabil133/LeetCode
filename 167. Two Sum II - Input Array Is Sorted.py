# get 2 sum that equal the target using left and right pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        ans = []
        while l != r:
            if numbers[l] + numbers[r] == target:
                ans = [l+1, r+1]
                return ans
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        return ans
