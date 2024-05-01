class Solution:
    def maxArea(self, height: List[int]) -> int:
        def getMin(a, b):
            if a <= b:
                return a
            return b
        one, tow = 0, len(height) - 1
        maxAmount = 0
        width = len(height) - 1
        while (one != tow):
            minHeight = getMin(height[one], height[tow])
            if (width * minHeight) > maxAmount:
                maxAmount = width * minHeight 
            width -= 1
            if height[one] == minHeight:
                one += 1
            else:
                tow -= 1
        return maxAmount 
