from typing import List 

class Solution:


    def hamming_weight(self,  n):
        count = 0   

        while n:
            n = n & (n-1)
            count += 1
        return count 
    
    def hamming_shift(self, n):
        res = 0 
        while n > 0:
            res += n % 2
            n = n >> 1
        return res