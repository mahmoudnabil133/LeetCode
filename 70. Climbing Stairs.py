# dinamic programing problems that calculate all posible ways that you can climb the stairs 
# given that you can step 1 or 2 steps in one time.
class Solution:
    def climbStairs(self, n: int) -> int:
        def steps(n, memo={}):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            elif n < 0:
                return 0
            x = steps(n-1, memo) + steps(n-2, memo)
            memo[n] = x
            return x
        num_steps = steps(n)
        return num_steps
