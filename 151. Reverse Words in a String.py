class Solution:
    def reverseWords(self, s: str) -> str:
        one, two = 0,0
        tot = ''
        while two < len(s):
            if tot:
                tot = ' ' + tot
            while two< len(s) and s[two] != ' ':
                two += 1
            new_str = s[one:two]
            tot = new_str + tot
 
            while two< len(s) and s[two] == ' ':
                two += 1
            one = two
        return tot
            
