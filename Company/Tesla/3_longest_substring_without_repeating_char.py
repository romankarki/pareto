class Solution:


    def len_of_substring(self, s: str) -> int: 
        # "abcabcbb" -> 3 "abc"
        # abca
        result = 0 
        l, r = 0, 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                result = max(result, r-l)
            else:
                seen.remove(s[l])
                l += 1 
        return result 
    

    def longest_substring_revision1(self, s: str) -> int: 
        longest = 0 
        l, r = 0, 0 
        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest = max(longest,len(seen) )
            else:
                seen.remove(s[l])
                l += 1 


        return longest 