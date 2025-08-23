public class Solution {
    public int LengthOfLastWord(string s) {
        int i = s.Length - 1, count=0;
        while(i>=0){
            while(i >= 0 && s[i] != ' '){
                count++;
                i--;
            }
            if(count > 0)
                return count;
            i--;
        }
        return count;
    }
}