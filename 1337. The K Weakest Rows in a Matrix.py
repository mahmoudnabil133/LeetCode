#!/usr/bin/python3
def kWeakestRows(mat, k):
    dic = {}
    for r in range(len(mat)):
        ones = mat[r].count(1)
        dic[r] = ones
    return sorted(dic.keys(), key=lambda x: dic[x])[:k]
        
print(kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2))
