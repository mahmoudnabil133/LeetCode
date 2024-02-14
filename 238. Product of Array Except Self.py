"on each index calculate product off other elements and return answer array"
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        flag = 0
        answer = []
        for i in range(len(nums)):
            if (nums[i] == 0):
                flag += 1
                continue
            mul *= nums[i]
        if flag > 1:
            mul = 0
        for i in range(len(nums)):
            if flag:
                if nums[i] == 0:
                    answer.append(mul)
                else:
                    answer.append(0)
            else:
                answer.append(mul // nums[i])
        return answer
