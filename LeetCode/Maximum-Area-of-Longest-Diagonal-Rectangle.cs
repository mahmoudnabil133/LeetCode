public class Solution {
    public int AreaOfMaxDiagonal(int[][] dimensions) {
        double maxDiagonal = 0, curDiagonal = 0;
        int maxArea = 0, curArea= 0;
        for(int i=0; i < dimensions.Length; i++){
            curDiagonal = Math.Sqrt((dimensions[i][0] * dimensions[i][0]) +(dimensions[i][1] * dimensions[i][1]) );
            curArea = dimensions[i][0] * dimensions[i][1];
            if(curDiagonal > maxDiagonal){
                maxDiagonal = curDiagonal;
                maxArea =  dimensions[i][0] * dimensions[i][1];
            } else if (curDiagonal == maxDiagonal){
                maxArea = (int) Math.Max(maxArea, curArea);
            }
        }
        return maxArea;
    }
}