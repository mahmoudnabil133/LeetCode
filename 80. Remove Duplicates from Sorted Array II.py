class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        index = 0
        print(dic)
        for elm in sorted(dic.keys()):
            if dic[elm] == 1:
                nums[index] = elm
                index += 1
            else:
                nums[index] = elm
                index += 1
                nums[index] = elm
                index+= 1
        return index
