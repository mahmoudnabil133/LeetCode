class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n

        for edge in roads:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
        degrees.sort()
        # smaller degrees takes smaller value
        val = 1
        tot_sum = 0
        for d in degrees:
            tot_sum += d * val
            val += 1
        return tot_sum