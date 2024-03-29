class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        "if target not found return the address that supposed to be right"
        if target > nums[mid]:
            return mid+1
        return mid
