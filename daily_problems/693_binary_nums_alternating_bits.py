class Solution:


    def has_alternating(self, n: int) -> bool:

        a = str(bin(n))
        s = a[2:]
        for i, each in enumerate(s):

            if i % 2 == 0 and s[i] != '1':
                return False 
            if i%2==0 and s[i] == '1':
                return False
        return True