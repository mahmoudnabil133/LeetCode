class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
           return False
        res = 0
        num = x
        while x > 0:
            y = x % 10
            x-=y
            x /= 10
            res = res*10 + y
        res = int(res)
        if (res - num == 0):
            return True
        
        return False
