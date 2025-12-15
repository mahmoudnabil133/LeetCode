1class Solution {
2public:
3    long long getDescentPeriods(vector<int>& prices) {
4        long long count = prices.size();
5        int l = 0; int r = 1;
6        while(r < prices.size()){
7            // cout<<"prices.size, prices[l], prices[r]: "<<prices.size()<<" "<<prices[l]<<" "<<prices[r]<<endl;
8            while(r < prices.size() && prices[r] == prices[r-1] - 1){
9                count+=(r-l);
10                r++;
11            }
12            l = r;
13            r++;
14        }
15        return count;
16    }
17};