public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int l = 0, r = 0;
        var set = new HashSet<char>();

        int count = 0, maxCount = 0;
        while(r < s.Length){
            while(r< s.Length && !set.Contains(s[r]))
            {
                set.Add(s[r]);
                r++;
                count++;
            }
            maxCount = Math.Max(maxCount, count);
            set.Remove(s[l]);
            count--;
            l++;
        }
        return maxCount;
    }
}