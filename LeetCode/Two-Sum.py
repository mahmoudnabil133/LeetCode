1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dic = {}
4        for i in range(0, len(nums), 1):
5            second_num = target - nums[i]
6            if(dic.get(second_num, -1) != -1):
7                return [i, dic[second_num]]
8            dic[nums[i]] = i
9        return [0, 0]