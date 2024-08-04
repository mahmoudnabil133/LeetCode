class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            res.append(nums[i])
            for j in range(i+1, n):
                res.append(nums[j] + res[-1])
        return sum(sorted(res)[left-1:right]) % ((10 ** 9) + 7)