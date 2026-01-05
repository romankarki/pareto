from collections import Counter

class Solution:


    def min_window(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        l, r = 0, 0 
        end = len(s) - 1
        c_t = Counter(t)

        res = ""
        c_s = {}
        min_len = float('inf')
        while r <= end:
            c_s[s[r]] = c_s.get(s[r], 0) + 1
            r += 1

            while self.matches(c_t, c_s):
                if (r-l) < min_len:
                    min_len = r - l
                    res = s[l:r]
                
                c_s[s[l]] -= 1
                l += 1
                
        return res

    def matches(self, c1: dict[str, int], c2 : dict[str, int]) -> bool:

        for k, v in c1.items():
            if k not in c2 or c2[k] == 0:
                return False
            if v > c2[k]:
                return False
        return True 