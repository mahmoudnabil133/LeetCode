1class Solution {
2public:
3    int maxArea(vector<int>& height) {
4        int l=0, r = height.size() -1;
5        int area, maxArea = 0;
6        while(l < r){
7            area = min(height[l], height[r]) * (r - l);
8            maxArea = max(maxArea, area);
9
10            if(height[l]<height[r]) l++; else r--;
11        }
12        return  maxArea;
13    }
14};