class Solution:


    def concatenation(self, n: int) -> int:

        s = ""

        for i in range(1, n+1):

            b = str(bin(i))
            s += b[2:]
        
        if s == "": 
            return 0

        modulo = 10**9 + 7
        return int(s, 2) % modulo