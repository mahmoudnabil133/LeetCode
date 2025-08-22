class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic =  {}
        max = 0
        for num in nums:
            if dic.get(num):
                dic[num] += 1
            else:
                dic[num] = 1
            if dic[num] > max:
                max = dic[num]
                major = num
        return major