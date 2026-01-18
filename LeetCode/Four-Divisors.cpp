1class Solution {
2public:
3    int sumFourDivisors(vector<int>& nums) {
4        int out = 0;
5
6        for(int i=0; i<nums.size(); i++){
7            out+= this->getDivisors(nums[i]);
8        }
9        return out;
10    }
11    int getDivisors(int n){
12        // vector<int> res;
13        int count=0, sum=1+n;
14        for(int i=2; i<=sqrt(n); i++){
15            if(n % i == 0){
16                count++;
17                sum+=i;
18                if(i * i != n){
19                    count++;
20                    sum += (n / i);
21                }
22            }
23        }
24        if (count == 2 ){        
25            return sum;
26        } else{
27            return 0;
28        }
29    }
30};