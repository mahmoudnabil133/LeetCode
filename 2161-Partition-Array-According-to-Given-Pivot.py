class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, g, e = [], [], []
        for n in nums:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                g.append(n)
            else:
                e.append(n)
        return l+e+g
