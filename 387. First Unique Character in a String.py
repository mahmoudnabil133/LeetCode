"return index of first unique character of string"
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
        for i in dic.keys():
            if dic[i] != -1:
                return dic[i]
        return -1
