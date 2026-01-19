1/*
2 * @lc app=leetcode id=34 lang=cpp
3 *
4 * [34] Find First and Last Position of Element in Sorted Array
5 */
6
7// @lc code=start
8class Solution {
9public:
10    vector<int> searchRange(vector<int>& nums, int target) {
11        int l=0, r = nums.size() - 1, mid = 0;
12        int ind = -1;
13        vector<int> ret;
14        
15        while(l<=r){
16            mid = l + (r-l)/2;
17            if (target > nums[mid]) l = mid+1;
18            else if(target < nums[mid]) r = mid-1;
19            else{
20                ind = mid;
21                break;
22            }
23        }
24        if (ind == -1){
25            ret = {-1, -1};
26        }else{
27            int left = ind;
28            int right = ind;
29            while(left > 0 && nums[left-1] == target) left--;
30            while(right<nums.size()-1 && nums[right+1] == target) right++;
31            cout<<left<<" "<<right<<endl;
32            ret = {left, right};
33        }
34        return ret;
35    }
36};
37
38