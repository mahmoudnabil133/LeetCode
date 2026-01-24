1class Solution {
2public:
3    bool searchMatrix(vector<vector<int>>& matrix, int target) {
4        for(int i=0; i<matrix.size(); i++){
5            int l=0;
6            int r = matrix[i].size() - 1;
7
8            while(l<=r){
9                int mid = l+ (r-l)/2;
10                if(target > matrix[i][mid]) l = mid+1;
11                else if(target < matrix[i][mid]) r = mid-1;
12                else return true;
13            }
14        }
15        return false;
16    }
17};