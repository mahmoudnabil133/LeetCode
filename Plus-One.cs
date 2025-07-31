using System.Numerics;
public class Solution {
    public int[] PlusOne(int[] digits) {
      int n = digits.Length;
      for(int i = n-1; i>=0; i--){
        if(digits[i] <9){
            digits[i] += 1;
            return digits;
        }
        digits[i] = 0;
      }
      // now all digits are 9

      int[] result = new int[n+1];
      result[0] = 1;
      return result;
    }
}