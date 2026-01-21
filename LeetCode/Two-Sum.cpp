1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        map<int, int> mp;
5        int secNum = 0;
6        for(int i=0; i<nums.size(); i++){
7            secNum = target - nums[i];
8            if(mp.count(secNum)) return {i, mp[secNum]};
9            mp[nums[i]] = i;
10        }
11        return {-1, -1};
12    }
13};