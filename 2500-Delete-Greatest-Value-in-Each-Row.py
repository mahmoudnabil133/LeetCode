class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sorted_rows = []
        for i in range(len(grid)):
            heap = []
            for j in range(len(grid[0])):
                heapq.heappush(heap, -1 * grid[i][j])
            sorted_rows.append(heap)
        
        ans = 0
        n = len(sorted_rows[0])
        for i in range(n):
            max_val = -1
            for hp in sorted_rows:
                max_val = max(max_val, -1* heapq.heappop(hp))
            ans += max_val
        return ans

