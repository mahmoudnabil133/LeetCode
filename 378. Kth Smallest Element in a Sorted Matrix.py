# meduim level :) haha
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([col for r in matrix for col in r])[k - 1]
