class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        min_deque = deque()
        max_deque = deque()
        long_diff = 0
        for r in range(len(nums)):
            # this append max and min according 2 its arrival
            while max_deque and nums[r] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[r])

            while min_deque and nums[r] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[r])

            while max_deque[0] - min_deque[0] > limit:
                if nums[l] == min_deque[0]:
                    min_deque.popleft()
                if nums[l] == max_deque[0]:
                    max_deque.popleft()
                l += 1
            long_diff = max(long_diff , r-l+1) 
        return long_diff
        #     heapq.heappush(min_heap, (nums[r], r))
        #     heapq.heappush(max_heap, (- nums[r], r))

        #     while -max_heap[0][0] - min_heap[0][0] > limit:
        #         # make left after than min (max , min) indexes
        #         l = min(min_heap[0][1], max_heap[0][1]) + 1
                
        #         # update top elements of min_heap and max_heap to remove elements 
        #         # before index left
        #         while min_heap[0][1] < l:
        #             heapq.heappop(min_heap)
        #         while max_heap[0][1] < l:
        #             heapq.heappop(max_heap)
        #     longest_diff_smaller_than_limit = max(longest_diff_smaller_than_limit, r - l +1)
        # return longest_diff_smaller_than_limit