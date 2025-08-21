public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int l=1, r = 1;

        while(r < nums.Length){
            while(r< nums.Length && nums[r] == nums[r-1])
                r++;
            if(r >= nums.Length)
                break;
            nums[l] = nums[r];
            l++;
            r++;
        }
        return l;
    }
}