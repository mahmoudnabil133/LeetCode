public class Solution {
    public int MajorityElement(int[] nums) {
        Array.Sort(nums);
        return nums[nums.Length/2];
        // var dic = new Dictionary<int, int>();
        // int maxFreq = 0, major = 0;
        // for(int i = 0; i< nums.Length; i++){
        //     if (dic.ContainsKey(nums[i]))
        //         dic[nums[i]] +=1;
        //     else
        //         dic[nums[i]] = 1;
        //     if (dic[nums[i]] > maxFreq){
        //         maxFreq= dic[nums[i]];
        //         major = nums[i];
        //     }
        // }
        // return  major;

    }
}