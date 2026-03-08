from typing import List

class Solution:


    def find_diff_binary_string(self, nums: List[str]) -> str: 
        n = len(nums)
        s = set(nums)

        for i in range(2**n):
            binary_str = bin(i)[2:]
            new_num = binary_str.zfill(n)
            
            if new_num not in s:
                return new_num
            
        return -1