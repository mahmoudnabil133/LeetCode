class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        diags = m+n-1
        i, j = 0, 0
        res = []

        for _ in range(diags):
            # up => i--, j++
            while i >= 0 and j <= m - 1:
                res.append(mat[i][j])
                i-=1
                j+=1
            
            i+=1
            j-=1

            # get starting point of diagnal
            if j < m-1:
                j+=1
            else:
                i+=1
            # down ==> i++, j--
            while i <= n-1 and j>= 0:
                res.append(mat[i][j])
                i+=1
                j-=1
            
            i-=1
            j+=1
            
            # get starting point of diagonal
            if i < n-1:
                i+=1
            else:
                j+=1
        return res
