class Solution:
    def clumsy(self, n: int) -> int:
        ops = []
        l = 0 
        ans = n
        result = 0
        for i in range(n-1, 0, -1):
            
            if l == 0:
                ans *= i
                
            elif l == 1:
                ans = int(ans / i)
             
            elif l==2:
                ans += i
                
            elif l == 3:
                result += ans
                ans = -i
            l += 1 
            l = l % 4

        result += ans 
        return result
        