1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        vector<int> out;
5        unordered_map<int, int> mp;
6        int temp;
7        for(int i =0; i<nums.size(); i++){
8            temp = target - nums[i];
9            if(mp.count(temp)){
10                out.push_back(mp[temp]);
11                out.push_back(i);
12                return out;
13            }
14            mp[nums[i]] = i;
15        }
16        return out;
17    }
18};