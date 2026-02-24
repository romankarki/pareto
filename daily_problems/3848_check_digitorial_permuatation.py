class Solution: 

    def is_digitorial_perm(self, n):
        if n ==0:
            return False 
        
        factorial = [1] * 10 

        for i in range(2, 10):
            factorial[i] = factorial[i-1] * i
        

        total = 0
        temp = n 

        while temp > 0:
            total += factorial[temp % 10]
            temp //= 10 
        

        return sorted(str(n)) == sorted(str(total))