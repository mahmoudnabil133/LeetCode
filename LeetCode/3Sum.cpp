1class Solution {
2public:
3    vector<vector<int>> threeSum(vector<int>& nums) {
4        sort(nums.begin(), nums.end());
5        vector<vector<int>> res;
6        int l,r;
7        for(int i=0; i<nums.size()-2;i++){
8            if(i>0 && nums[i] == nums[i-1]) continue;
9            l = i+1;
10            r = nums.size() - 1;
11            int tot;
12            while(l<r){
13                tot = nums[i] + nums[l] + nums[r];
14                if(tot > 0) r--;
15                else if (tot < 0) l++;
16                else {
17                    res.push_back({nums[i], nums[l], nums[r]});
18                    while(l<r && nums[r] == nums[r-1]) r--;
19                    while(l <r && nums[l] == nums[l+1]) l++;
20                    l++;
21                    r--;
22                }
23            }
24        }
25        return res;
26    }
27};