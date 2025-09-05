public class Solution {
    public int MaxArea(int[] height) {
        int maxArea = 0, currentArea = 0;
        int l = 0, r = height.Length - 1;
        while(l<r)
        {
            currentArea = Math.Min(height[l], height[r]) * (r - l);
            maxArea = Math.Max(currentArea, maxArea);
            if (height[l] > height[r])
                r--;
            else
                l++;
        }
        return maxArea;
    }
}