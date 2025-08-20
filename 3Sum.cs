public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        var result = new List<IList<int>>();

        for(int i =0; i< nums.Length - 2; i++){
            if (i > 0 && nums[i] == nums[i-1] )
                continue;
            
            int l = i+1, r = nums.Length -1, tot = 0;

            while(l < r){
                tot = nums[i] + nums[l] + nums[r];
                if(tot < 0)
                    l++;
                else if(tot > 0)
                    r--;
                else{
                    result.Add([nums[i], nums[l], nums[r]]);
                    while (l < r && nums[l + 1] == nums[l])
                        l++;
                    while( r > l && nums[r - 1] == nums[r])
                        r--;
                    l++;
                    r--;
                    
                }
            }
        }
        return result;
    }
}