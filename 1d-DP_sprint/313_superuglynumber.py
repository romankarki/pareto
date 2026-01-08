from typing import List

class Solution: 

    def nth_super_ugly(self, n: int, primes: List[int]) -> int:

        dp  = [ 1 ] * n 

        i_primes = [0] * len(primes)
        next_primes = [0] * len(primes)


        for i in range(1, n):
            for j in range(0, len(primes)): 
                next_primes[j] = dp[i_primes[j]] * primes[j]
            
            dp[i] = min(next_primes)

            for j in range(0, len(primes)): 
                if dp[i] == next_primes[j]: 
                    i_primes[j] += 1

        return dp[-1]
    


s = Solution()

print(s.nth_super_ugly(12, [2,7,13,19]))