1class Solution {
2public:
3
4    int org_color, new_color;
5    int rows, cols;
6    vector<vector<int>> *img;
7    // cell should be as original to fill ==> (*img)[i][j] != org_color
8    void dfs(int i, int j){
9        if(i < 0 || i>= rows || j<0 || j>= cols || (*img)[i][j] != org_color) 
10            return;
11
12        (*img)[i][j] = new_color;
13        
14        dfs(i-1, j);
15        dfs(i, j+1);
16        dfs(i+1, j);
17        dfs(i, j-1);
18    }
19    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
20
21        org_color = image[sr][sc];
22        rows = image.size();
23        cols = image[0].size();
24        new_color = color;
25        img = &image;
26
27
28        // if new color same as original so no need to flood fill
29        if(org_color == new_color){
30            return image;
31        }
32        dfs(sr, sc);
33        return image;
34    }
35};