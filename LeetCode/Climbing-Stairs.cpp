1class Solution {
2public:
3    int climbStairs(int n) {
4        vector<int>v(n+1,0);
5        v[0] = 1;
6        v[1] = 1;
7
8        for(int i=2; i<=n;i++){
9            v[i] = v[i-1] + v[i-2];
10        }
11        return v[n];
12    }
13};