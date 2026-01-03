
class Solution:


    def reverse_prefix(self, s: str, k: int) -> str:
        rev = self.reverse(s[0: k])
        ans = rev + s[k: len(s)]
        return ans 
    
    def reverse(self, ms: str):
        ans = ""
        for i in range(len(ms)-1, -1, -1):
            ans += ms[i]
        return ans 