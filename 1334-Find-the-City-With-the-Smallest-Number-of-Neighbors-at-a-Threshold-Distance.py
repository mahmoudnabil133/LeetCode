class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        prev_mat = []
        for i in range(n):
            l = []
            for j in range(n):
                if i == j:
                    l.append(0)
                else:
                    l.append(float("inf"))
            prev_mat.append(l)

        for ed in edges:
            prev_mat[ed[0]][ed[1]] = ed[2]
            prev_mat[ed[1]][ed[0]] = ed[2]

        for k in range(n):
            cur_mat = prev_mat.copy()
            for i in range(n):
                for j in range(n):
                    if i == j:
                        cur_mat[i][j] = 0
                    elif i == k or j == k:
                        cur_mat[i][j] = prev_mat[i][j]
                    else:
                        cur_mat[i][j] = min(prev_mat[i][j], prev_mat[i][k] + prev_mat[k][j])
            prev_mat = cur_mat

        smallest_neighbors_num = float("inf")
        city = 0
        for i in range(n):
            allowed_neighbors = 0
            for j in range(n):
                if prev_mat[i][j] <= distanceThreshold:
                    allowed_neighbors += 1
            if allowed_neighbors <= smallest_neighbors_num:
                smallest_neighbors_num = allowed_neighbors
                city = i
        return city