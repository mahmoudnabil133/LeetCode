"""
you are given int and you should return num of
ones of its binary representation
---Sol--
convert num to bin --(how):
get reminder of num by 2 and append left to get bin
and devide by num by 2 each iteration
then iterate Binary to get ones sum
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        mul = 1
        Bin = 0
        while n:
            rem = n % 2
            Bin += (rem * mul)
            mul *= 10
            n //= 2

        ones = 0
        while Bin:
            top = Bin % 10
            if top == 1:
                ones += 1
            Bin //= 10
        return ones

        