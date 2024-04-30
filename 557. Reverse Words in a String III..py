class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ''
        word = ''
        rev_word = ''
        rev = False
        spaces = 0
        for i in range(len(s)):
            if s[i] == ' ':
                print('space', i)
                rev = True
                if spaces != 0:
                    new_str += ' '
                spaces +=1

            else:
                rev = False
                word += s[i]
            if rev or i == len(s)-1:
                print(word)
                if len(s)-1 == i and new_str:
                    word+=' '
                rev_word = word[::-1]
                print(rev_word)
                new_str += rev_word
                word = ''
        return new_str
