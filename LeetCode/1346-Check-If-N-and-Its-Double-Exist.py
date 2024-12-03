class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for d in arr:
            if 2 * d in s or (d / 2) in s:
                return True
            s.add(d)
        return False