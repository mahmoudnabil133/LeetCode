class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            else:
                freq[num] += 1
                return num
