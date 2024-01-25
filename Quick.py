#!/usr/bin/python3
"""
O(nlog(n)) in
worst Case: if arr is sorted it will be O(N^2)
unlike mergeSort is always (O(nlog(n))) but its problem is aspace complexty
it needs an auxalary space o(n) beacouse of creating left and righ list recursivly
then you merge the list accendingly
"""
def quick(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]
    return quick(less) + [pivot] + quick(greater)
arr = quick([1,7,2,4,6,8,0])
print(arr)
