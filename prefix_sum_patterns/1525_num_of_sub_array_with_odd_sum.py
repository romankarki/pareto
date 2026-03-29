from typing import List 


class Solution: 
    def num_of_subarray(self, arr: List[int]) -> int: 
        MOD = 10**9 + 7 
        running_sum = 0 
        odd_count = 0 
        even_count = 1 
        result = 0 

        for num in arr:
            running_sum += num 

            if running_sum % 2 == 0:
                result += odd_count 
                even_count += 1
            else: 
                result += even_count 
                odd_count += 1

        result %= MOD 
        return result 