public class Solution {
    public bool CanJump(int[] nums) {
       int maxJump = 0;
       for (int i=0; i<nums.Length; i++){
            if(maxJump <0)
                return false;
            maxJump = Math.Max(maxJump, nums[i]);
            maxJump--;
       } 
       return true;
    }
}