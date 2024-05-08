class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft = [0] * n
        sumRight = [0] * n

        totLeft , totRight = 0, sum(nums)

        for i in range(len(nums)):
            sumLeft[i] = totLeft
            totLeft += nums[i]
            totRight -= nums[i]
            sumRight[i] = totRight
            if sumLeft[i] == sumRight[i]:
                return i
        return -1
