public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int sumLeft = 0, sumRight = nums.Sum();
        var res = new List<int>();
        foreach(var n in nums){
            sumRight -= n;
            res.Add(Math.Abs(sumRight - sumLeft));
            sumLeft+=n;
        }
        return res.ToArray();
    }
}