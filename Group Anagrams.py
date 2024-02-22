class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            dic[sorted_str].append(s)
        return list(dic.values())
