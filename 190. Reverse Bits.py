"""
geven an int convert it to bin
then revrese the bin then add zeros 
then cinvert it again to int
last thing return the reversed int
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        mul = 1
        Bin = 0
        dig = 0
        """
        covert int to bin dig var to get sum of left zeroz
        now it doesnt have meaning but in reversed bin it will
        be important 
        """
        while n:
            dig +=1
            rem = n % 2
            Bin += (rem * mul)
            mul *= 10
            n //= 2
        loop = 32 - dig
        mul2 = 1
        "delete right zeroz as it will be ignored in reversed bin"
        while Bin:
            top = Bin % 10
            if top == 1:
                break
            Bin //= 10
        "rev a Bin and get rev_bin"
        rev_bin = 0
        while Bin:
            top = Bin % 10    
            rev_bin = ((rev_bin * mul2) + top)
            mul2 = 10
            Bin //= 10
        "add zeros to reversed bin"
        for i in range(loop):
            rev_bin *= 10
        rev_int = 0
        
        "finaly convert a rev_bin to int and optain rev_int"
        mul3 = 1
        while rev_bin:
            top = rev_bin % 10
            rev_int += (top * mul3)
            mul3 *= 2
            rev_bin //= 10
        return rev_int
