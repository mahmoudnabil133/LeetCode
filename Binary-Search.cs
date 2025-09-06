public class Solution {
    public int Search(int[] nums, int target) {
        int l=0, r = nums.Length - 1, i, mid;
        while (l<= r){
            // i = (r+l)/2; // if r and l is int.MaxValue this will make bug (overflow) and res will be negative
            i = l+(r-l)/2;
            mid = nums[i];

            if( target < mid)
                r = i-1;
            else if (target >mid)
                l = i+1;
            else
                return i;
        }
        return -1;
        
    }
}