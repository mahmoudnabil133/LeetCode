class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        orgGrid = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                orgGrid[i][j] = min(rowSum[i], colSum[j])

                rowSum[i] -= orgGrid[i][j]
                colSum[j] -= orgGrid[i][j]
        return orgGrid