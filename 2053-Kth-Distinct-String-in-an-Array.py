class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = {}
        for el in arr:
            dic[el] = dic.get(el, 0) + 1
        dis = []
        for key in dic.keys():
            if dic[key] == 1:
                dis.append(key)
        # print(k, len(dis))
        if k > len(dis):
            return ""
        return dis[k-1]