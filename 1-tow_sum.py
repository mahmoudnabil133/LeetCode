class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    output.append(i)
                    output.append(j)
        return output
        