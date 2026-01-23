1class Solution {
2public:
3    int oldColor;
4    vector<vector<int>> img;
5    int newColor;
6    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
7        img = image;
8        newColor = color;
9        oldColor = image[sr][sc];
10        if(oldColor == color) return image;
11        dfs(sr, sc);
12        return img;
13    }
14    void dfs(int r, int c){
15        if(r<0 || r>= img.size() || c<0 || c>=img[0].size() || img[r][c] != oldColor) return;
16        img[r][c] = newColor;
17        dfs(r-1, c);
18        dfs(r+1, c);
19        dfs(r, c-1);
20        dfs(r, c+1);        
21    }
22};