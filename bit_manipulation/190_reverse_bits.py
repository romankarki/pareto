class Solution:

    def reverse_bits(self, n):
        res = 0 
        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31-i))

        return res 