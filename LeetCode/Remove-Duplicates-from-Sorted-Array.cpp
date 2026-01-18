1class Solution {
2public:
3    int removeDuplicates(vector<int>& nums) {
4        int l = 1;
5        int k = 0;
6        int r = 1;
7        while(r<nums.size()){
8            while(r< nums.size() && nums[r] == nums[r-1]) r++;
9
10            if (r>= nums.size()) return l;
11            nums[l] = nums[r];
12            l++;
13            r++;
14
15        }
16        return l;
17    }
18};