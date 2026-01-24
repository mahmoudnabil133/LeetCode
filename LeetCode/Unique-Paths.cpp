1class Solution {
2public:
3    int uniquePaths(int m, int n) {
4        vector<vector<int>> dp(m, vector<int>(n, 0));
5        dp[0][0] = 1;
6        int left, top;
7        for(int i=0; i<m;i++){
8            for(int j = 0; j<n; j++){
9                if(i==0&&j==0) continue;
10                left = 0, top = 0;
11                if(i-1>=0){
12                    top=dp[i-1][j];
13                }
14                if(j-1>=0){
15                    left=dp[i][j-1];
16                }
17                dp[i][j] = left + top;
18            }
19        }
20        return dp[m-1][n-1];
21    }
22};