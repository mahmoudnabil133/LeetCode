1class Solution {
2public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        unordered_map<string, vector<string>> mp;
5        vector<vector<string>> res;
6        string temp;
7
8        for (auto s:strs){
9            temp = s;
10            sort(s.begin(), s.end());
11            if(mp.count(s)) mp[s].push_back(temp);
12            else mp[s] = {temp};
13        }
14        for (auto it:mp){
15            res.push_back(it.second);
16        }
17        return res;
18        
19    }
20};