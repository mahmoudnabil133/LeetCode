class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        out = []
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        sorted_values = sorted(dic, key= lambda x: (dic[x], -x))

        for v in sorted_values:
            out += [v] * dic[v]
        return out
