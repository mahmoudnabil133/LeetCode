class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top , buttom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) -1
        res = []

        while len(res) < len(matrix) * len (matrix[0]):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top +=1 
            for i in range(top, buttom+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= buttom:
                for i in range(right, left-1, -1):
                    res.append(matrix[buttom][i])
                buttom -=1
            if left <= right:
                for i in range(buttom, top - 1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res 
