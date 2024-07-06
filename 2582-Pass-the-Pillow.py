class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 1
        direction = -1

        for count in range(time):
            if cur == 1 or cur == n:
                direction *= -1
            cur += direction
        return cur