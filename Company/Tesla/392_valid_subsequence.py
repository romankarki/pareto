class Solution:

    def is_subsequence(self, s: str, t : str) -> bool:
        i = 0 
        j = 0 
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
    
    def is_subsequence_revision1(self, s: str, t:str) -> bool:

        i, j = 0, 0 

        while i < len(s) and j < len(t):
            if s[i] == s[j]:
                i += 1
            j += 1
        return i == len(s)