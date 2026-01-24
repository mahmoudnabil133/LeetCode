1class Solution {
2public:
3    int search(vector<int>& nums, int target) {
4        int l =0;
5        int r = nums.size()-1;
6
7        while(l<=r){
8            int mid = l+(r-l)/2;
9            if(target < nums[mid]) r = mid-1;
10            else if(target > nums[mid]) l = mid+1;
11            else return mid;
12            cout<<mid<<endl;
13        }
14        return -1;
15    }
16};