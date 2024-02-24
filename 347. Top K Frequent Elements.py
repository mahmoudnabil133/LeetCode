class Solution:
    def topKFrequent(self, nums):
        dic = {}
        # hash map (dictionary) to count frequincies of each item
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        # sort dic acording to values(second parameter)
        new_dic = dict(sorted(dic.items(), key=lambda item: item[1]))
        l = list(new_dic.keys())
        # return k keys with beggest values (we sliced it from end dict is sorted ascendingly)
        return l[len(l)-k:]
