public class Solution {
    public void MoveZeroes(int[] nums) {
        int n = nums.Length;
        int l = 0;
        int r = 0;

        while(r < n){
            while(r < n && nums[r] != 0){
                nums[l]= nums[r];
                if (r > l){
                    nums[r] = 0;
                }
                l++;
                r++;
            }
            while( r < n && nums[r] == 0){
                r++;
            }
        }
    }
}