class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        min_heap = []
        max_heap  = []
        longest_diff_smaller_than_limit = 0
        for r in range(len(nums)):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (- nums[r], r))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                # make left after than min (max , min) indexes
                l = min(min_heap[0][1], max_heap[0][1]) + 1
                
                # update top elements of min_heap and max_heap to remove elements 
                # before index left
                while min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
            longest_diff_smaller_than_limit = max(longest_diff_smaller_than_limit, r - l +1)
        return longest_diff_smaller_than_limit