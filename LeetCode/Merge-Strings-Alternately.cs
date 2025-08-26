public class Solution {
    public string MergeAlternately(string word1, string word2) {
        int l = 0, r = 0, len1 = word1.Length, len2 = word2.Length;
        string result = "";
        while(l < len1 && r<len2){
            result+=word1[l];
            result+=word2[r];
            l++;
            r++;
        }
        if(l < len1){
            result+=word1.Substring(l, len1 - l);
        } else if (r<len2){
            result+=word2.Substring(r, len2 - r);
        }
        return result;
    //     while(l < len1 && r<len2){
    //         while(l < len1 && word1[1] < word2[r]){
    //             result+= word1[l];
    //             l++;
    //         }
    //         if(l == len1){
    //             break;
    //         }

    //         while(r<len2 && word2[r] < word1[l]){
    //             result+=word2[r];
    //             r++;
    //         }
    //     }
    //     while(l<len1){
    //         result+=word1[l];
    //         l++;
    //     }
    //     while(r<len2){
    //         result+=word2[r];
    //         r++;
    //     }
    //     return result;
    // }
}
}