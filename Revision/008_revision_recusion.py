class Solution:


    def fib(self, n):
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)
    
    def fib_dp(self, n):
        memo = {}

        def helper(n):

            if n<=1:
                return n
            
            if n in memo:
                return memo[n]
            
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fib_simple(self, n):
        if n <= 1:
            return n
        
        return self.fib_simple(n-1) + self.fib_simple(n-2)
    
