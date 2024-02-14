"check if there is a dublicate in array"
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums)) < len(nums)):
            return True
        return False
