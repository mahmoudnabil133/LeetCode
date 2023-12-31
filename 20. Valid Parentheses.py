class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                opened = stack.pop()

                if (i==')' and opened != '('):
                    return False
                
                if (i=='}' and opened != '{'):
                    return False

                if (i == ']' and opened != '['):
                    return False
        if stack:
            return False
        return True

    