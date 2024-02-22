class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) -1
            while l < r:
                tot = nums[i]+ nums[l] + nums[r]
                if tot < 0:
                    l+=1
                elif tot > 0:
                    r-=1
                else:
                    out.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l+=1
                    while l< r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return out
# print(Sum([1,-1,2,-2,-3,-1,3,-4,2]))
# #!/usr/bin/python3
# def Sum(nums):
    # out = []
    # sorted = []
    # for i in range(len(nums) - 2):
    #     for j in range(i + 1, len(nums) - 1):
    #         for k in range(j + 1, len(nums)):
    #             new_list = []
    #             if (nums[i] + nums[j] + nums[k] == 0):
    #                 new_list.append(nums[i])
    #                 new_list.append(nums[j])
    #                 new_list.append(nums[k])
    #                 cp = new_list.copy()
    #                 cp.sort()
    #                 if cp not in sorted:
    #                     out.append(new_list)
    #                     sorted.append(cp)
    # return out

# print(Sum([1,-1,2,-2,-3,-1,3,-4,2]))
