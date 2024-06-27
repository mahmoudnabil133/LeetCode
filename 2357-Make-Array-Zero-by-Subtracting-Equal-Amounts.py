class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            if i:
                heapq.heappush(heap, i)
        ans = 0
        while heap:
            ans += 1
            new = []
            smallest = heapq.heappop(heap)
            for i in range(len(heap)):
                if heap[i] - smallest > 0:
                    new.append(heap[i] - smallest)
            heap = new
            heapq.heapify(heap)
        return ans
        