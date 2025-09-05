public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        var sorted = nums.OrderBy(x=>x).ToArray();
        var map = new Dictionary<int, int>();
        for(int i=0; i<sorted.Length; i++){
            if(!map.ContainsKey(sorted[i]))
                map[sorted[i]] = i;
        }
        return nums.Select(x=> map[x]).ToArray();
    }
}