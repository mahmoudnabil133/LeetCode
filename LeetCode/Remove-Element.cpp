1class Solution {
2public:
3    int removeElement(vector<int>& nums, int val) {
4        int l = 0;
5        int k = 0;
6        for(int r=0; r<nums.size(); r++){
7            if(nums[r] != val){
8                nums[l] = nums[r];
9                l++;
10                k++;
11            }
12        }
13        return k;
14    }
15};