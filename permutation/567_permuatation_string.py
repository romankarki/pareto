from collections import Counter


class Solution:

    def check_inclusion(self, s1: str, s2:str):
        # time -> O(n* k)
        # space -> O(n)
        k= len(s1)
        c1 = Counter(s1)
        l, r = 0, len(s2) - 1
        while l <= r and (l+k-1)<=r:
            curr = s2[l:l+k]
            c2 = Counter(curr)
            if c1 == c2:
                return True
            
            l += 1
        return False
