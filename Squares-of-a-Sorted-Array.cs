public class Solution {
    public int[] SortedSquares(int[] nums) {
        int n  = nums.Length;
        for(int j=0; j<nums.Length; j++){
            nums[j] *= nums[j];
        }

        int[] output = new int[n];
        int i = n -1;
        int l =0;
        int r = n-1;

        while(l <= r){
            if(nums[r] > nums[l])
            {
                output[i] = nums[r];
                i--;
                r--;
            }else{
                output[i] = nums[l];
                l++;
                i--;
            }
        }
        return output;
    }
}