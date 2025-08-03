public class Solution {
    public void ReverseString(char[] s) {
        int l = 0;
        int r = s.Length - 1;
        char temp;
        while(l< r){
            temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }
    }
}