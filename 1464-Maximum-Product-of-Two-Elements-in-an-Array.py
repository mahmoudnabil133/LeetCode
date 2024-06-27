class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)

        one = heapq.heappop(heap)*-1 - 1
        two = heapq.heappop(heap)*-1 - 1
        return one * two
