from typing import List 


class Solution: 
    def num_of_subarray(self, arr: List[int]) -> int:
        '''
        I scan the array and see check each array is even or odd and respectively add even_count += 1 or odd_count +=1 if even or odd 

        if even then all the odd possibilites with this even also makes odd so result += odd_count 
        if odd  then all the even possibilities with this odd makes odd so result += even_count

        and even_count start with 1 as 0 is even
        ''' 
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