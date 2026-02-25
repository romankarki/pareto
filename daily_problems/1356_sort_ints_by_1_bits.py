from typing import List 
from collections import Counter

class Solution:

    def sort_bits(self, arr: List[int]) -> List[int]:
        count = {}

        for each in arr:
            s = str(bin(each))
            e = s[2:]
            c_count = Counter(e)

            ones = str(c_count['1'])
            if ones not in count:
                count[ones] = []
            count[ones].append(each)
        
        ff = sorted(count.keys(), key= int)

        result = []
        for each in ff:
            dd = count[each].copy()
            dd.sort()
            result += dd 
            
        return result