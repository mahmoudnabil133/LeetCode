class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        i = 0
        map_nums = {}
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) +1
            key = n
            val = 0
            mul = 1
            if not n:
                val = mapping[n]
            while n:
                dig = n % 10
                n //= 10
                val += (mapping[dig] * mul)
                mul *= 10
            map_nums[key] = val
        unique_nums = sorted(map_nums, key= lambda x: map_nums[x])

        out = []
        for num in unique_nums:
            out += [num] * freq[num]
        return out