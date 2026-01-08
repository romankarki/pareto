import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

         # helper lcm or we can use math lcm I guess
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        # count of ugly numbers <= x
        def count(x):
            return (x // a + x // b + x // c
                    - x // ab - x // bc - x // ac
                    + x // abc)
        
        l, r = 0, 2 * (10**9)
        while l < r: 
            mid = (l + r) // 2
            if count(mid) < n: 
                l = mid + 1
            else: 
                r = mid 

        return l