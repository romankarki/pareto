class Solution:

    def valid_anagram(self, s:str, t: str) -> bool:
        if len(s) != len(t): return False

        h1 = [0] * 26
        h2 = [0] * 20

        for i in range(0, len(s)):
            h1[ord(t[i]) - ord('a')] += 1
            h2[ord(s[i]) - ord('a')]  +=1 

        return h1 == h2