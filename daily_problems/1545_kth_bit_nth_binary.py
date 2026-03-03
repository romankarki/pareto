class Solution:


    def find_kth_bit(self, n: int, k: int):
        s = "0"
        for i in range(1,n):
            new_s = self.invert_reverse(s)
            s = s + "1" + new_s
        return s[k-1]
    


    def invert_reverse(self, s):
        n_s = ""

        for each in s:
            if each == "0":
                n_s += "1"
            else:
                n_s += "0"
        return n_s[::-1]
