from typing import List 


class Solution:

    def min_deleteion(self, s: str) -> int: 

        total_a = s.count('a')
        min_deletions = total_a

        b_count = 0 

        for char in s: 
            if char == 'a':
                total_a -= 1
            else: 
                b_count += 1
            min_deletions = min(min_deletions, b_count + total_a)
        return min_deletions

    def minimumDeletions(self, s: str) -> int:
        violate_a = 0 

        for each in s: 
            if each == "a":
                violate_a += 1
        ans = violate_a
        violate_b = 0 

        for char in s: 
            if char == "a":
                violate_a -= 1
            else: 
                violate_b += 1
            
            ans = min(ans, violate_a + violate_b)
        return ans 