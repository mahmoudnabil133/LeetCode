class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # for odd subs
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            # for even subs
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            
        return res
