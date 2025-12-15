1class Solution {
2public:
3    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
4        if (k<=1) return 0;
5        int l=0; 
6        int ans=0;
7        int mul= 1;
8
9        for(int r=0; r<nums.size(); r++){
10            mul *= nums[r];
11
12            while(mul >= k){
13                mul /=nums[l];
14                l++;
15            }
16            ans += (r-l +1);
17        }
18        return ans;
19
20    }
21};