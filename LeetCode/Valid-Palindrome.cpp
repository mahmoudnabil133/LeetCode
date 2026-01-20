1class Solution {
2public:
3    bool isPalindrome(string s) {
4        int l=0, r = s.size()-1;
5        while(l<r){
6            while (l<s.size() && !(s[l]>='0' && s[l]<='9') && !((s[l] >= 'A' && s[l] <= 'Z') || (s[l] >= 'a' )))  l++;
7            while(r>0 && !(s[r]>='0' && s[r] <= '9') &&!((s[r] >= 'A' && s[r] <= 'Z') || (s[r] >= 'a' && s[r] <= 'z'))) r--;
8            
9            if(l>=s.size() || r< 0 || l>=r) return true;
10            if(tolower(s[l]) == tolower(s[r])){
11                l++;
12                r--;
13            }
14            else return false;
15        }
16        return true;
17    }
18};