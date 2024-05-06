class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one, two = 0, 0
        ans = []
        while one < m and two < n:
            if nums1[one] < nums2[two]:
                ans.append(nums1[one])
                one += 1
            elif nums1[one] >= nums2[two]:
                ans.append(nums2[two])
                two += 1
        while one < m:
            ans.append(nums1[one])
            one += 1
        while two < n:
            ans.append(nums2[two])
            two += 1

        for i in range(len(ans)):
            nums1[i] = ans[i]
        print(ans)
