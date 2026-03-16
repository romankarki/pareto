from typing import List 

class Solution:


    def hamming_weight(self,  n):
        count = 0   

        while n:
            n = n & (n-1)
            count += 1
        return count 