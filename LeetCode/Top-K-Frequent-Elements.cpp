1class Solution {
2public:
3    vector<int> topKFrequent(vector<int>& nums, int k) {
4        unordered_map<int, int> mp;
5        for(auto n:nums){
6            mp[n]++;
7        }
8
9        priority_queue<pair<int, int>> pq;
10        vector<int> res;
11
12        for(auto [k, v]: mp){
13            pq.push(make_pair(v, k));
14        }
15
16        while(k--){
17            res.push_back(pq.top().second);
18            pq.pop();
19        }
20        return res;
21    }
22};