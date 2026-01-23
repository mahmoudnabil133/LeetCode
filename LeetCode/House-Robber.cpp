1class Solution {
2public:
3    int rob(vector<int>& nums) {
4        int sz = nums.size();
5        if(sz==1) return nums[0];
6        nums[1] = max(nums[0],nums[1]);
7        for(int i=2; i<sz; i++){
8            nums[i]= max(nums[i]+ nums[i-2], nums[i-1]);
9        }
10        return max(nums[sz-1], nums[sz-2]);
11    }
12};