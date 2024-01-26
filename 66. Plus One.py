"""
steps to solve
list to int
add one
int to list
reverse list
return
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mul = 1
        sum = 0
        while digits:
            num = digits.pop()
            sum += (num * mul)
            mul *= 10
        sum += 1
        output = []
        while sum:
            num = sum % 10
            output.append(num)
            sum //= 10
        print(output, sum )
        output.reverse()

        return output
