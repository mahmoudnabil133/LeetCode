"""
mediam level
find the lenght of longest substring not repeated
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" :
            return 0

        output = [1]
        for i in range (len(s) -1):
            num = 1
            j = i + 1
            str1 = s[i]
            while(j < len(s)):
                if s[j] not in str1:
                   num += 1
                   str1 += s[j]
                else:
                    break
                j += 1
            output.append(num)
            output.sort(reverse=True)

        return output[0]
