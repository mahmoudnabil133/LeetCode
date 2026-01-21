1class Solution {
2public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        map<string, vector<string>> mp;
5        vector<vector<string>> res;
6        string temp;
7
8        for (auto s:strs){
9            temp = s;
10            sort(s.begin(), s.end());
11            if(mp.count(s)){
12                mp[s].push_back(temp);
13            } else{
14                mp[s] = {temp};
15            }
16        }
17        for (auto it:mp){
18            res.push_back(it.second);
19        }
20        return res;
21        
22    }
23};