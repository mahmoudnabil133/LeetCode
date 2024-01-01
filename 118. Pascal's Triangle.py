class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[] for i in range(numRows)]
        pascal[0].append(1)
        if numRows == 1:
            return pascal

        for i in range(numRows-1):
            x = pascal[i]
            y = pascal[i+1]
            y.append(1)
            for j in range(len(x)-1):
                y.append(x[j] + x[j+1])
            y.append(1)
        return pascal
