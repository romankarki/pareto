from typing import List


class Solution:

    def sum_of_divisors(self, nums: List[int]) -> int:
        total = 0 

        for each in nums:
            if each > 6:
                continue 

            divisors = set()

            for i in range(1, int(each ** 0.5)+1):
                if each % i == 0:
                    divisors.add(i)
                    divisors.add(each // i)
                    if len(divisors) > 4:
                        break
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total 