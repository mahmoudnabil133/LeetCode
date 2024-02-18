class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(' ')
        while l[-1] == '':
           l.pop()
        if len(l) <1:
            return 0
        return len(l[-1])
