class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack =[]
        for c in s:
            if c == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
        return ''.join(stack)
        # opened = 0
        # out = ''
        # no_par = ''
        # tot_out = ''
        # x=''
        # i = 0
        # while i < len(s): 
        #     while i < len(s) and s[i] == '(':
        #         opened += 1
        #         i += 1
        #         print(s[i+1])
        #     print(opened)
        #     start_open = opened
        #     while opened > 0:
        #         even = ''
        #         ev_flag = False
        #         od_flag = False
        #         while i< len(s) and opened > 0 and opened %2 == 0:
        #             ev_flag = True
        #             while i < len(s) and s[i] == ')':
        #                 opened -= 1
        #                 i+=1
        #             print('1')
        #             if opened %2 == 1:
        #                 break
        #             while i < len(s) and s[i] == '(':
        #                 opened += 1
        #                 i+=1
        #             print('2')
        #             if opened %2 == 1:
        #                 break
        #             even+= s[i]
        #             i+=1
        #         if opened == start_open and ev_flag:
        #             print('he')
        #             out = even+odd+out
        #             odd = ''
        #             even = ''
        #             break
        #         odd = ''
        #         while i < len(s) and  opened  > 0 and opened %2 ==1:
        #             od_flag = True
        #             while i < len(s) and s[i] == ')':
        #                 opened -= 1
        #                 i+=1
        #             print('3')
        #             if opened %2 == 0:
        #                 break
        #             while i < len(s) and s[i] == '(':
        #                 opened += 1
        #                 i+=1
        #             print('4')
        #             if opened %2 == 0:
        #                 break
        #             odd = s[i] + odd
        #             i+=1
        #         print('out', out)
        #         print('even', even)
        #         print('odd', odd)
        #         out = even+odd + out
        #         even = ''
        #         odd = ''
        #     while i < len(s) and opened == 0:
        #         if s[i] == '(':
        #             opened +=1
        #             i+=1
        #             break
        #         no_par+=s[i]
        #         i+=1
        #     if no_par:
        #         tot_out += out + no_par
        #         print(tot_out, out, no_par, 'hererere')
        #         out=''
        #     # if no_par:
        #     no_par = ''
        # if tot_out:
        #     out = tot_out + out
        # return out
            
