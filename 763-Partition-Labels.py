class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        ans = []
        l = 0

        while l < len(s):
            new_part = {}
            r = l
            while new_part.get(s[l], 0) < dic.get(s[l], 0) and r < len(s):
                new_part[s[r]] = new_part.get(s[r], 0) + 1
                r += 1
            keys = list(new_part.keys())
            while keys:
                k = keys.pop()
                while new_part.get(k, 0) < dic.get(k, 0) and r < len(s):
                    if not new_part.get(s[r], 0):
                        keys.append(s[r])
                    new_part[s[r]] = new_part.get(s[r], 0) + 1
                    r += 1
            ans.append(r-l)
            l = r
        return ans