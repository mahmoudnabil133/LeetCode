"reverse int (medium problem)"
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        flag = 0
        edge = 2147483648
        if x < 0:
            x *= -1
            flag = 1
        while(x > 0):
            digit = x % 10
            x /= 10
            result = result * 10 + digit
        if flag:
             result *= -1
        if result <  -1 * edge or result > edge:
            return 0
       
        return result
        