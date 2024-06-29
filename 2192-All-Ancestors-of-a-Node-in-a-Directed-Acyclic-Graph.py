class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def dfs(start, curr, visit):
            visit[curr] = True
            for son in graph[curr]:
                if not visit[son]:
                    res[son].append(start)
                    dfs(start, son, visit)
        
        graph = [[] for _ in range(n)]
        res = [[] for _ in range(n)]

        for e in edges:
            graph[e[0]].append(e[1])
        
        for i in range(n):
            dfs(i, i, [False]*n)
        return res