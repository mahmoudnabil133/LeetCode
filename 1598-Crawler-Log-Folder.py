class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == './' or (ans == 0 and log == '../'):
                continue
            elif log == '../':
                ans -= 1
            else:
                ans +=1
        return ans