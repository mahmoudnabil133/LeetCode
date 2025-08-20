public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        var dic = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++ ){
            int diff = target - nums[i];

            if(dic.ContainsKey(diff))
                return [dic[diff], i];
            
            dic[nums[i]] = i;
        }
        return [];
    }
}