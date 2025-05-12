class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        even = []
        out = set()
        dic = {}
        for d  in digits:
            if dic.get(d):
                dic[d] += 1
            else:
                dic[d] = 1
        for n in range(100, 999, 2):
            even.append(n)

        for e in even:
            s_dic = {}
            dig1 = e // 100
            dig2 = (e // 10) % 10
            dig3 = e % 10
            digs = [dig1, dig2, dig3]

            for d in digs:
                if s_dic.get(d):
                    s_dic[d] += 1
                else:
                    s_dic[d] = 1
            flag = 0
            for k in s_dic.keys():

                if not dic.get(k) or  s_dic[k] > dic[k]:
                    flag = 1
                    break
            if not flag:
                out.add(e)
        return sorted(list(out))

        # brute force (TLE answer)
        # output = []
        # n = len(digits)
        # for i in range(n):
        #     if digits[i] == 0:
        #         continue
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         for k in range(n):
        #             if k == j or k == i:
        #                 continue
        #             num = digits[i] * 100 + digits[j] * 10 + digits[k]
        #             if num not in output and num % 2 == 0:
        #                 output.append(num)
        #                 print(output)
        # return sorted(output)              