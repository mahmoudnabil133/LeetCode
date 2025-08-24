public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int l = 0, minSize = int.MaxValue, subSum = 0;

        for(int r = 0; r < nums.Length; r++){
            subSum += nums[r];

            while(subSum >= target){
                minSize = Math.Min(minSize, r-l+1);
                subSum -= nums[l];
                l++;    
            }
        }
        return minSize == int.MaxValue? 0 : minSize;
}
}