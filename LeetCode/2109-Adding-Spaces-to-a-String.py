class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = ""
        j = 0

        for i in range(len(s)):
            if i == spaces[j]:
                out += " "
                j+=1
            if j == len(spaces):
                out+= s[i:]
                return out
            out+= s[i]
        return out