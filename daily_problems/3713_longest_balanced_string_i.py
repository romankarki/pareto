class Solution:
    def longestBalanced(self, s: str) -> int:

        '''
        string = abbacddc
        '''


        ans = float("-inf")
        if len(s) == 1:
            return 1
        for i in range(0, len(s)-1):
            freq = {}
            l = 0 
            for j in range(i, len(s)):
                l += 1
                freq[s[j]] = freq.get(s[j], 0) + 1
                if (self.is_balanced(freq)):
                    ans = max(ans, l)
        return ans 
    

    def is_balanced(self, freq):

        if len(freq.values()) == 0:
            return True 
       
        first = None
        for each in freq.values():
            if first is None:
                first = each 
                continue
            if each != first:
                return False 
        return True 
        


        