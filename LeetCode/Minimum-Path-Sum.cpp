1class Solution {
2public:
3    int minPathSum(vector<vector<int>>& grid) {
4        int m = grid.size();
5        int n = grid[0].size();
6
7        vector<vector<int>> dp(m, vector<int>(n, 0));
8        dp[0][0] = grid[0][0];
9        for(int i=0; i<m;i++){
10            for(int j=0; j<n; j++){
11                if(i==0&&j==0) continue;
12
13                if(i-1 < 0) dp[i][j] = dp[i][j-1] + grid[i][j];
14                else if(j-1 < 0) dp[i][j] = dp[i-1][j] + grid[i][j];
15                else dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
16            }
17        }
18        return dp[m-1][n-1];
19    }
20};