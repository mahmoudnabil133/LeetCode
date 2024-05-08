class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = ''
        new_str = ''
        for i in range(len(word)):
            if word[i] != ch:
                rev += word[i]
            else:
                rev += word[i]
                new_str = rev[::-1]
                new_str += word[i+1:]
                return new_str
        return word
