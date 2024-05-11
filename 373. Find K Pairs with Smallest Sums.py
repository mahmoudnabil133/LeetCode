class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # return sorted([ [x, y] for x in nums1 for y in nums2 ], key = lambda res: res[0]+res[1] )[:k]
        ans = []
        visited = set()
        hp = []
        heapq.heappush(hp, (nums1[0]+nums2[0], (0, 0)))
        visited.add((0, 0))

        while k and hp:
            val, (i, j) = heapq.heappop(hp)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(hp, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(hp, (nums1[i]+ nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
            k-=1
        return ans 
