#!/usr/bin/env python3
"convert from integer to roman string "
class Solution:
    def intToRoman(self, num: int) -> str:
        dec = {'M':1000,'CM':900,'D':500,'CD':400,
        'C':100, 'XC':90, 'L':50,'XL':40,'X':10,
        'IX':9, 'V':5,'IV':4, 'I':1}
        out = ''
        for k in dec.keys():
            sym_nums = num // dec[k]
            out += k * sym_nums
            num %= dec[k]
        return out
s = Solution()
print(s.intToRoman(133))
