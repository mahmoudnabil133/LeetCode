public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int n = nums.Length;
        int i = 0; 
        int k = 0;

        while(i < n){
            while(i < n-1 && nums[i] == nums[i+1]){
                i++;
            }
            nums[k] = nums[i];
            k++;
            i++;
        }
        return k;
    }
}