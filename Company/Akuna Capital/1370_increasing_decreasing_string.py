from collections import Counter
import string 

class Solution:


    def increasing_decreasing_sort(self, s: str) -> str: 

        c = Counter(s)
        ans = ''
        # alphabets  =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphabets = string.ascii_lowercase
        iteration = 1 

        while len(ans) < len(s):

            build = ''
            data  = alphabets if iteration % 2 == 1 else reversed(alphabets)

            for each in data:
                if each in c and c[each] > 0:
                    build += each 
                    c[each] -= 1
            ans += build 
            iteration += 1
        return ans