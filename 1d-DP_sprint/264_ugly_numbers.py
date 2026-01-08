class Solution: 

    def nth_ugly_dp(self, n: int) -> int :
        dp = [1] * n
        i2 = i3 = i5 = 0 

        for i in range(1, n): 
            next2 = dp[i2] * 2
            next3 = dp[i3] * 3
            next5 = dp[i5] * 5

            dp[i] = min(next2, next3, next5)

            if dp[i]  == next2: 
                i2 += 1
            if dp[i] == next3: 
                i3 += 1
            if dp[i] == next5: 
                i5 += 1


        return dp[-1] 

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
    


    def nth_ugly_num(self, n: int) -> int: 
        dp = [1] * n 

        i2 = i3 = i5 = 0 

        for i in range(1, n): 
            next2 = dp[i2] * 2
            next3 = dp[i3] * 3
            next5 = dp[i5] * 5

            dp[i] = min(next2, next3, next5)

            if dp[i] == next2: 
                i2 += 1
            if dp[i] == next3: 
                i3 += 1
            
            if dp[i] == next5: 
                i5 +=1


        return dp[-1]