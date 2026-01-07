class Solution: 

    def nth_ugly_number(self, n: int) -> int: 

        ans = [] 
        i= 1
        while len(ans) < n: 
            if self.is_ugly(i):
                ans.append(i)
            i += 1
        return ans [-1]
    
    def is_ugly(self, n): 
        s = [2,3,5]
        for p in s: 
            while n % p == 0:
                n //= p 
        return n == 1