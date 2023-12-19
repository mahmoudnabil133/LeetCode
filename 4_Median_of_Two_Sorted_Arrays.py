#!/usr/bin/python3
"""
(Hard) level Proplem
merge 2 sorted arrays
# output [] list to contain the the merge , sorted list
# iterate them parallel untill we finish one of them
# then append the other one to the list
# then we find the median of the merged list and return
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        output = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j += 1
    
        while i < len(nums1):
            output.append(nums1[i])
            i += 1

        while j < len(nums2):
            output.append(nums2[j])
            j += 1
        "Handle if lenght if merged arr  is odd or even"
        if len(output) % 2 != 0:
            index = int(len(output) / 2)
            median = output[index]
        
        else:
            ind1 = int(len(output) /2)
            ind2 = ind1 - 1
            median = (output[ind1] + output[ind2]) / 2
        ret = float(median)
        return ret
