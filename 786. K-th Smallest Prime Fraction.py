class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        arr2 = [[arr[i]/arr[j], arr[i], arr[j]] for i in range(len(arr) - 1) for j in range (i + 1, len(arr))]
        heapq.heapify(arr2)
        while k:
            smallest = heapq.heappop(arr2)
            one = smallest[1]
            two = smallest[2]
            k-=1
        return [one, two]
        
