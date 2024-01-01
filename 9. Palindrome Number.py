class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        y = xstr
        y = ''.join(reversed(y))
        if (y == xstr):
            return True
        return False

        