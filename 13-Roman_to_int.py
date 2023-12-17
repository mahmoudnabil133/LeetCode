class Solution(object):
    def romanToInt(self, s):
        sum = 0
        x = 0
        l = 0
        for i in s:
            if i == 'I':
                x = 1
            elif i == 'V':
                x = 5
            elif i == 'X':
                x = 10
            elif i == 'L':
                x = 50
            elif i == 'C':
                x = 100
            elif i == 'D':
                x = 500
            elif i == 'M':
                x = 1000
        
            if i == 'V' or i == 'X':
                if l == 'I':
                    x -= 2
                    
            if i == 'L' or i == 'C':
                if l == 'X':
                    x -= 20
            if i == 'D' or i == 'M':
                if l == 'C':
                    x -= 200
            l = i
            sum += x
        return sum
            
        