class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l, r = 0, 0
        out = []

        while l < len(nums1) and r < len(nums2):
            while l < len(nums1) and nums1[l] < nums2[r]:
                l += 1
            if l >= len(nums1):
                break
            
            while r < len(nums2) and nums2[r] < nums1[l]:
                r += 1
            if r >= len(nums2):
                break
            if nums1[l] == nums2[r]:
                out.append(nums1[l])
                l+=1
                r+=1
        return out