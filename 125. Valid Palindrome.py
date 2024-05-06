class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.lower()
        ptr1 = 0
        ptr2 = len(new_str) - 1

        while ptr1 != ptr2:
            while ptr1 < len(new_str) and not (new_str[ptr1].isalpha() or new_str[ptr1].isdigit()):
                ptr1 += 1

            while ptr2 > -1 and not (new_str[ptr2].isalpha() or new_str[ptr2].isdigit()):
                ptr2 -= 1

            if ptr1 == ptr2:
                break
            
            if ptr1 >= len(new_str) and ptr2 < 0:
                break

            if new_str[ptr1] == new_str[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True
