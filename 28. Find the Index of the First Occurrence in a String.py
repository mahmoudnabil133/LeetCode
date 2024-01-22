class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sub_len = len(needle)
        for i in range(len(haystack)- sub_len + 1):
            end = i + sub_len
            if needle == haystack[i:end]:
                return i
        return -1
        