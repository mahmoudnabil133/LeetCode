1class Solution {
2public:
3    int minCostClimbingStairs(vector<int>& cost) {
4        int n = cost.size()+ 1;
5        vector<int> dp(n, 0);
6        dp[0] = cost[0];
7        dp[1] = cost[1];
8        for(int i=2; i<n-1; i++){
9            dp[i] = min(dp[i-1], dp[i-2])+cost[i];
10        }
11        dp[n-1]=min(dp[n-2], dp[n-3]);
12        return dp[n-1];
13    }
14};